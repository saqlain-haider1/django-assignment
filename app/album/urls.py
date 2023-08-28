from django.urls import path
from .views import create_album
urlpatterns = [
    path('', create_album, name='create_album'),
]
