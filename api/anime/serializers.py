from rest_framework import serializers 
from .models import Anime
 
 
class AnimeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Anime
        fields = ('title', 'type', 'score', 'episodes', 'image_url','synopsis', 'airing', 'url')

