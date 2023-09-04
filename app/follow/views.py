from django.shortcuts import render


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Album, Follow
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404

# Create your views here


class FollowAlbumView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlbumSerializer

    def create(self, request, album_id):
        album = get_object_or_404(Album, id=album_id)

        user = request.user
        if Follow.objects.filter(user=user, album=album).exists():
            return Response({"message": "You are already following this album!"}, status=status.HTTP_400_BAD_REQUEST)

        follower = Follow(user=user, album=album)
        follower.save()

        return Response({"message": "You are now following this album!"}, status=status.HTTP_201_CREATED)
