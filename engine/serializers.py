from rest_framework import serializers
from engine.models import Film
from .models import FilmMarker

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmMarkerSerializer(serializers.ModelSerializer):
    film = FilmSerializer()  # 包括电影的详细信息

    class Meta:
        model = FilmMarker
        fields = ['id', 'user_id', 'film']
