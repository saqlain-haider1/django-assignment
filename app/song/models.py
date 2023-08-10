from django.db import models

from tag.models import Tag

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
