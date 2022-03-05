from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import User, Category, Course, Lesson, Tag
from django import forms
from django.urls import path
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created_date')
    list_filter = ('id', 'name', 'created_date')


class CourseAdmin(admin.ModelAdmin):
    search_field = ['subject', 'category'],
    readonly_fields = ['image_view']

    def image_view(self, course):
        if course:
            return mark_safe(
            '<img src="/static/{url}" width="120" />'\
            .format(url=course.image.name)
            )

    def get_urls(self):
        return [
            path('course-stats/', self.stat_view)
        ] + super().get_urls()

    def stat_view(self, request):
        c = Course.objects.filter(active=True).count()
        stats = Course.objects.annotate(lesson_count=Count('my_lesson')).values('id', 'subject', 'lesson_count')

        return TemplateResponse(request,
                                'admin/course-stats.html', {
                                    'count': c,
                                    'stats': stats
                                })


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)