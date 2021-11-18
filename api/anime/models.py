from os import name
from django.db import models
from django.db.models.fields import CharField, IntegerField, URLField, related

# Create your models here.

ANIME_TYPES = [
    ("Movie", "Movie"),
    ("OVA", "OVA"),
    ("Special", "Special"),
    ("ONA", "ONA"),
    ("TV", "TV"),
]

class Anime(models.Model):
    title = models.CharField(max_length=200, blank=False, default ='')
    type = models.CharField(max_length=7, choices=ANIME_TYPES)
    score = models.CharField(max_length=5, default='')
    episodes = models.IntegerField(default=0) 
    image_url = models.URLField(max_length=255)
    airing = models.BooleanField(default = False)
    synopsis = models.CharField(max_length=255, default ='')
    url = models.URLField(max_length=255)

