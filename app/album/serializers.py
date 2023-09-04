
from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(allow_null=True, default=None, read_only=True)

    class Meta:
        model = Album
        fields = ['owner', 'title', 'songs', 'is_public', 'created_at']
