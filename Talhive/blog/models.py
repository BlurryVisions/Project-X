from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title