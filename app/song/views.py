from .models import Song
from .serializers import SongSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from authentication.permissions import IsAdminUser

# Create your views here.


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class SongSearchFilterView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        title_query = self.request.query_params.get('title')
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)

        tags_query = self.request.query_params.getlist('tags')

        if tags_query:
            queryset = queryset.filter(tags__name__in=tags_query)

        return queryset


class ScheduleSongView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        song_id = self.kwargs['song_id']
        song = get_object_or_404(Song, pk=song_id)
        if song:
            return Response({"message": "Song added to scheduled songs list."}, status=status.HTTP_201_CREATED)
