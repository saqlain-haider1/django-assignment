from django.urls import path
from .views import (
    AddSongToFavoriteView
)
urlpatterns = [
    path('<int:song_id>/', AddSongToFavoriteView.as_view(), name='add_sonsg_to_favorites'),
]
