from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import AlbumSerializer
from .models import Album
# Create your views here.


class AlbumCreateListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
