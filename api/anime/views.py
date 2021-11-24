from django.db.models.query import QuerySet
from django.http import JsonResponse
from pandas.io import api
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .recommendation import recommendAnime
from .models import Anime
from .serializers import AnimeSerializer, RecommendSerializer

# Create your views here.
#post and get requests are handled

class AnimeListCreate(APIView):

    def get(self, request):
        line = request.get_full_path()
        find = line.split('/')[-1]
        title = find[7:].title()
        titles = Anime.objects.filter(title=title).values() #filters data
        if str(titles) == '':
            return Response('No anime found') 
        else:
            return Response(titles)

class AnimeListRecommend(APIView):

    def get(self, request, title):
        title = title.title()
        animeList = recommendAnime(title)
        return Response(animeList)
