from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NotesModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
