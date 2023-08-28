from song.models import Song
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import render
from .models import Favorite
from rest_framework import generics
# Create your views here.

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Song, Favorite
from .serializers import FavoriteSerializer


class AddSongToFavoriteView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        song_id = self.kwargs['song_id']
        return Favorite.objects.filter(song_id=song_id, user=self.request.user)

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        serializer.save(song=song, user=self.request.user)

    def post(self, request, *args, **kwargs):
        already_in_favorite = self.get_queryset()
        if already_in_favorite.exists():
            return Response({"message": "Song is already in Favorite collection!"}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
