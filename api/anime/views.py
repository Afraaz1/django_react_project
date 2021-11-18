from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Anime
from .serializers import AnimeSerializer

# Create your views here.
#post and get requests are handled
class AnimeListCreate(ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
