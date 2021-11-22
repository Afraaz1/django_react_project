from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListCreateAPIView
from scipy.sparse import data
from .recommendation import lookUpAnime
from .models import Anime
from .serializers import AnimeSerializer

# Create your views here.
#post and get requests are handled

class AnimeListCreate(ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


@api_view(['GET', 'POST'])
def AnimeRecommend(request):

    if request.method == 'GET':
        title = request.GET['title']
        results = lookUpAnime(title)
        serializer = AnimeSerializer(results, data=data)
        return JsonResponse(serializers.data)

    if request.method =='POST':
        serializer = AnimeSerializer.objects.all()
        return JsonResponse(serializer.data)

@api_view(['GET', 'POST'])
def AnimeRecommend(request):

    if request.method == 'GET':
        title = request.GET['title']
        results = lookUpAnime(title)
        serializer = AnimeSerializer(results, data=data)
        return JsonResponse(serializers.data)

    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)