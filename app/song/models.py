from django.utils import timezone
from django.db import models

from tag.models import Tag

# Create your models here.


class ReleasedSongManager(models.Manager):
    def get_queryset(self):
        current_date = timezone.now().date()
        return super().get_queryset().filter(release_date__lte=current_date)


class Song(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField(default=timezone.now().date())

    objects = ReleasedSongManager()
