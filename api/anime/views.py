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
    #On get requests sends data
    def get(self, request):

        #In order to find the query
        line = request.get_full_path()
        find = line.split('/')[-1]
        title = find.title()

        #Ensuring that inputted title exists
        if(bool(title)):
            titles = Anime.objects.filter(title__icontains=title).values() #filters data
            return Response(titles)
        else:
            return Response("No data found")
    
class AnimeListRecommend(APIView):
    
    def get(self, request, title):
        #getting parameters from title
        title = title.title()
        animeList = recommendAnime(title)
        data = []

        #filters list to return all the data of the recommended list to pass to frontend
        for anime in animeList:
            anime = anime.title()
            animeData = Anime.objects.filter(title=anime).values()
            data.append(animeData)
        return Response(data)

@api_view(['GET'])
def anime_detail(request, pk):
    #Ensures primary key exists before returning data, error if it doesnt
    try:
        anime = Anime.objects.get(pk=pk)
    except Anime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #If data requested is valid return database data
    if request.method == 'GET':
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)