from django.contrib import admin
from .models import User, Category, Course

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created_date')
    list_filter = ('id', 'name', 'created_date')

admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)