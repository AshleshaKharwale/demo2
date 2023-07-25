from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
