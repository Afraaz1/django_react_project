from anime import views 
from django.urls import path
from anime.views import AnimeListCreate


urlpatterns = [ 
    path('api/anime/', views.AnimeListCreate.as_view())
]
