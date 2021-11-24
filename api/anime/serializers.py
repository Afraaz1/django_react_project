from rest_framework import serializers 
from .models import Anime, Recommend
 
 
class AnimeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Anime
        fields = ('title', 'image_url', 'rating', 'airing','broadcast', 'score')

class RecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommend
        fields = ('title', 'anime_id')