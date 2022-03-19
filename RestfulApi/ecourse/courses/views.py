from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Course, Lesson, Comment
from .serializers import (CategorySerializer,
                          CourseSerializer,
                          LessonSerializer,
                          LessonDetailSerializer,
                          CommentSerializer,
                          CreateCommentSerializer)
from .paginators import CoursePaginator
from .perms import CommentOwnerPermisson

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            query = query.filter(name__icontains=kw)

        return query


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            query = query.filter(subject__icontains=kw)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = query.filter(category_id=cate_id)

        return query

    @action(methods=['get'], detail=True, url_path='lessons')
    def get_lessons(self, request, pk):
        #c = Course.objects.get(pk=pk)
        c = self.get_object()
        lessons = c.lessons

        return Response(data=LessonSerializer(lessons, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailSerializer

    @action(methods=['get'], url_path='comments', detail=True)
    def get_comment(self, request, pk):
        lesson = self.get_object()
        comments = lesson.comments.select_related('user')

        return Response(CommentSerializer(comments, many=True).data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CreateCommentSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            # kiem tra request.user co phai owner cua comment
            return [CommentOwnerPermisson()]

        return [permissions.IsAuthenticated()]