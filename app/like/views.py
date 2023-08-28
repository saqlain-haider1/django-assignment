from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like
from song.models import Song
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Song, Like
from like.serializers import LikeSerializer


class LikeSongView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        return Like.objects.filter(song_id=song_id, user=self.request.user)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        serializer.save(song=song, user=self.request.user)

    def post(self, request, *args, **kwargs):
        existing_likes = self.get_queryset()
        if existing_likes.exists():
            return Response({"message": "You've already liked this song"}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def like_song(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     user = request.user
#     # TODO: Check if the user has already liked the song
#     if Like.objects.filter(user=user, song=song).exists():
#         return Response({"message": "You've already liked this song"}, status=status.HTTP_400_BAD_REQUEST)
#     like = Like(song=song, user=user)
#     like.save()

#     return Response({"message": "Song liked successfully"}, status=status.HTTP_200_OK)
