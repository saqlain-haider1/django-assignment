from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like
from song.models import Song
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_song(request, song_id):
    song = Song.objects.get(id=song_id)
    user = User.objects.get(username=request.user.username)
    # TODO: Check if the user has already liked the song

    like = Like(song=song, user=user)
    like.save()

    return Response({"message": "Song liked successfully"}, status=status.HTTP_200_OK)
