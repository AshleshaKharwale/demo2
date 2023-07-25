from django.contrib import admin
from .models import NotesModel
# Register your models here.

@admin.register(NotesModel)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'modified']
    