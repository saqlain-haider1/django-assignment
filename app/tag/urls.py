from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', TagViewSet, basename="tag")
urlpatterns = [
    path('', include(router.urls)),
]
