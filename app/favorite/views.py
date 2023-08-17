from song.models import Song
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import render
from .models import Favorite
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_sonsg_to_favorite(request, song_id):
    song = Song.objects.get(id=song_id)
    if not song:
        return Response({"message": "Song not found!"}, status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if Favorite.objects.filter(user=user, song=song).exists():
        return Response({"message": "Song is already added to favorites!"}, status=status.HTTP_400_BAD_REQUEST)

    favorite = Favorite(user=user, song=song)
    favorite.save()

    return Response({"message": "Song added to favorites successfuly!"}, status=status.HTTP_201_CREATED)
