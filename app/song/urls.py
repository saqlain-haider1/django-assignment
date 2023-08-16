from django.urls import path
from .views import (
    get_all_songs,
    search_filter_songs,
)

urlpatterns = [
    path('', get_all_songs, name='get_all_songs'),
    path('search/', search_filter_songs, name='search_filter_songs'),
]
