from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    pass


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(ModelBase):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(ModelBase):
    subject = models.CharField(max_length=255)
    description =models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='course/%Y%m')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('subject', 'category')

    def __str__(self):
        return self.subject


class Lesson(ModelBase):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to='course/%Y%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', related_query_name='my_lesson')
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(ModelBase):
    content = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content