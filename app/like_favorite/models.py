from django.db import models
from django.contrib.auth.models import User
from song.models import Song
# Create your models here.


class LikeAndFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    is_liked = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
