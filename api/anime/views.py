from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from scipy.sparse import data
from .recommendation import lookUpAnime
from .models import Anime
from .serializers import AnimeSerializer

# Create your views here.
#post and get requests are handled

class AnimeListCreate(ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer



class AnimeRecommend(APIView):

    @api_view(['GET', 'POST'])
    def get(self, request):
        title = request.GET['title']
        results = lookUpAnime(title)
        serializer = AnimeSerializer(results)
        return Response(serializers.data)

    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)