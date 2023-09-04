from django.urls import path
from .views import (
    AlbumCreateListView
)
urlpatterns = [
    path('', AlbumCreateListView.as_view(), name='create_album'),
]
