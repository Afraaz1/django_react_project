from anime import views 
from django.urls import path, re_path
from .views import AnimeListCreate, AnimeListRecommend


urlpatterns = [ 
    re_path('api/anime/.', AnimeListCreate.as_view()),
    path('recommend/<str:title>', AnimeListRecommend.as_view(), name='recommend')
    ]
