from rest_framework import serializers 
from .models import Anime
 
 
class AnimeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Anime
        fields = ('title', 'synopsis', 'airing')