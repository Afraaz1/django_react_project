from anime import views 
from django.urls import path
from .views import AnimeRecommend, AnimeListCreate


urlpatterns = [ 
    path('api/anime/', views.AnimeListCreate.as_view()),
    path('api/anime/recommend', views.AnimeRecommend())
]
