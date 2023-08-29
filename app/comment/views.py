from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from song.models import Song

from .serializers import CommentSerializer
# Create your views here.


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        serializer.save(song=song, user=self.request.user)

    def post(self, request, *args, **kwargs):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        if not song:
            return Response({"message": "Song not found!"}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
