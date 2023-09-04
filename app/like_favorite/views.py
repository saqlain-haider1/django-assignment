from .models import LikeAndFavorite
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from song.models import Song
from rest_framework.generics import CreateAPIView
from like_favorite.serializers import LikeFavoriteSerializer
# Create your views here.


class LikeSongView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeFavoriteSerializer

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        return LikeAndFavorite.objects.filter(song_id=song_id, user=self.request.user)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        serializer.save(song=song, user=self.request.user, is_liked=True)

    def post(self, request, *args, **kwargs):
        existing_song = self.get_queryset().first()  # Get the first matching song (if any)
        if existing_song:
            if existing_song.is_liked:  # Check if the user has already liked the song
                return Response({"message": "You've already liked this song"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # If the user had previously disliked the song, update it to be liked
                existing_song.is_liked = True
                existing_song.save()
                return Response({"message": "Song liked successfully!"}, status=status.HTTP_200_OK)
        else:
            # Create a new record
            return super().post(request, *args, **kwargs)


class AddSongToFavoriteView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeFavoriteSerializer

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        return LikeAndFavorite.objects.filter(song_id=song_id, user=self.request.user)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        serializer.save(song=song, user=self.request.user, is_favorite=True)

    def post(self, request, *args, **kwargs):
        existing_favorite = self.get_queryset().first()  # Get the first matching song (if any)
        if existing_favorite:
            if existing_favorite.is_favorite:  # Check if the song is already in favorites
                return Response({"message": "Song is already in Favorite collection!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # If the user had previously removed the song from favorites, update it to be a favorite again
                existing_favorite.is_favorite = True
                existing_favorite.save()
                return Response({"message": "Song added to Favorite collection!"}, status=status.HTTP_200_OK)
        else:
            # Create a new record
            return super().post(request, *args, **kwargs)
