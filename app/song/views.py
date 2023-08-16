from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_filter_songs(request):
    title_query = request.query_params.get('title', '')
    tags_query = request.query_params.getlist('tags')
    songs = Song.objects.all()

    if title_query:
        songs = songs.filter(title__icontains=title_query)

    if tags_query:
        songs = songs.filter(tags__name__in=tags_query)

    serialized_songs = SongSerializer(songs, many=True)
    return Response(serialized_songs.data)
