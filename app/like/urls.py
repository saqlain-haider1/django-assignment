from django.urls import path
from .views import like_song
urlpatterns = [
    path('<int:song_id>/', like_song, name='like_song'),
]
