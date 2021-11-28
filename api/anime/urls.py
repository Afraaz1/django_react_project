from anime import views 
from django.urls import path, re_path
from .views import AnimeListCreate, AnimeListRecommend
from anime import views


urlpatterns = [ 
    re_path('anime/.', AnimeListCreate.as_view()),
    path('anime/recommend/<str:title>', AnimeListRecommend.as_view(), name='recommend'),
    path('anime/anime_id/<int:pk>', views.anime_detail, name='anime_id'),
    ]


