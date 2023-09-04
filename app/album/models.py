from django.db import models
from django.contrib.auth.models import User
from song.models import Song
# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    songs = models.ManyToManyField(Song, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
