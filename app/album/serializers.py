
from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    # owner = serializers.CharField(source='owner.name', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Album
        fields = ['owner', 'title', 'songs', 'is_public', 'created_at']
