from django.db import models

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=32, default='untitled', unique=True)
    nav_name = models.CharField(max_length=32, default='Untitled')
    content = models.TextField(max_length=8192, default='Hello, World!')
    position = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

