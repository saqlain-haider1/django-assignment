
from django.urls import path
from .views import (
    CommentListCreateView
)
urlpatterns = [
    path('<int:song_id>/', CommentListCreateView.as_view(), name='create_comment'),
]
