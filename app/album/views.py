from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer
from .models import Album
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_album(request):

    album_serializer = AlbumSerializer(data=request.data)
    if album_serializer.is_valid():
        title = request.data.get('title')
        owner = request.user
        is_public = request.data.get('is_public')

        album = Album(title=title, owner=owner, is_public=is_public)
        album.save()

        return Response({"message": "Album created successfully!"}, status=status.HTTP_201_CREATED)

    return Response(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
