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
#Specificing data so that no incorrect data can be inputted
SOURCE_TYPES = [
    ("Original", "Original"),
    ("Manga", "Manga"),
    ("Game", "Game"),
    ("Unknown", "Unknown"),
    ("Web manga", "Web manga"),
    ("Light novel", "Light novel"),
    ("Other", "Other"),
    ("Visual Novel", "Visual Novel"),
    ("Music", "Music"),
]
STATUS = [
    ("Finished Airing", "Finished Airing"),
    ("Currently Airing", "Currently Airing"),
    ("Not yet aired", "Not yet aired"),
]

#Declaring database fields
class Anime(models.Model):
    anime_id = models.IntegerField(max_length=11, primary_key=True)
    title = models.CharField(max_length=200, blank=False, default ='')
    title_english = models.CharField(max_length=200, default ='')
    title_japanese = models.CharField(max_length=200, default ='')
    title_synonyms = models.CharField(max_length=200, default ='')
    image_url= models.URLField(max_length=255, default ='')
    type = models.CharField(choices=ANIME_TYPES, max_length=200, default ='')
    source = models.CharField(choices=SOURCE_TYPES, max_length=200, default ='')
    episodes = models.IntegerField(default ='0')
    status = models.CharField(choices=STATUS, max_length=200, default ='')
    airing = models.BooleanField(default = False)
    aired_string = models.CharField(max_length=200, default ='')
    aired = models.CharField(max_length=200, default ='')
    duration = models.CharField(max_length=200, default ='')
    rating = models.CharField(max_length=100, default ='')
    score = models.CharField(max_length=5, default ='')
    scored_by = models.IntegerField(default =0)
    rank = models.IntegerField(default =0)
    popularity = models.IntegerField(default =0)
    members = models.IntegerField(default =0)
    favorites = models.IntegerField(default =0)
    snyopsis = models.CharField(max_length=200, default ='')
    premiered = models.CharField(max_length=200, default ='')
    broadcast = models.CharField(max_length=200, default ='')
    related = models.CharField(max_length=300, default ='')
    producer = models.CharField(max_length=200, default ='')
    licensor = models.CharField(max_length=200, default ='')
    studio = models.CharField(max_length=200, default ='')
    genre = models.CharField(max_length=300, default ='')

#Declaring recommend database fields
class Recommend(models.Model):
    header = models.CharField(max_length=200, blank=False, default='')
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)

    

