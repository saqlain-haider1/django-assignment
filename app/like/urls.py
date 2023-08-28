from django.urls import path
from .views import (
    LikeSongView
)
urlpatterns = [
    path('<int:song_id>/', LikeSongView.as_view(), name='like_song'),
]
