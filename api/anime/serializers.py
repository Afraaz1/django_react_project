from rest_framework import serializers 
from .models import Anime, Recommend
 
 
# Anime model serialiser, when used with data returns all the fields specified.
class AnimeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Anime
        fields = [ 'title', 'image_url', 'rating', 'airing','broadcast', 'score']


# Recommend model serializer to return data with all the fields
class RecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommend
        fields = ('title', 'anime_id')