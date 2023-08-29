from django.urls import path
from .views import (
    SongList,
    SongSearchFilterView,
    ScheduleSongView
)

urlpatterns = [
    path('', SongList.as_view(), name='get_all_songs'),
    path('search/', SongSearchFilterView.as_view(), name='search_filter_songs'),
    path('schedule/<int:song_id>/', ScheduleSongView.as_view(), name='schedule'),

]
