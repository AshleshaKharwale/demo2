from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
from .models import Blog, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published', 'updated']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


# Generating drf authtoken for all users
TokenAdmin.raw_id_fields = ['user']
