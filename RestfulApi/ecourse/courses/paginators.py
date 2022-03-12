from rest_framework import pagination

class CoursePaginator(pagination.PageNumberPagination):
    page_size = 1
    page_query_param = 'page'