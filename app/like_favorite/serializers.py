from rest_framework import serializers
from .models import LikeAndFavorite


class LikeFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeAndFavorite
        fields = '__all__'
