from django.urls import path
from .views import add_sonsg_to_favorite
urlpatterns = [
    path('<int:song_id>/', add_sonsg_to_favorite, name='add_sonsg_to_favorites'),
]
