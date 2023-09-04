from django.urls import path
from .views import FollowAlbumView

urlpatterns = [
    path('<int:album_id>/', FollowAlbumView.as_view(), name='follow-album'),
]
