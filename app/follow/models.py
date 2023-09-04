from django.db import models
from album.models import Album

from django.contrib.auth.models import User

# Create your models here.


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
