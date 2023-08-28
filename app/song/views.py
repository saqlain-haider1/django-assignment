from django.shortcuts import render

from .models import Song
from .serializers import SongSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters

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
