from django.db import models

from django.contrib.auth.models import User
from song.models import Song
# Create your models here.


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
