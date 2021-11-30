from anime import views 
from django.urls import path, re_path
from .views import AnimeListCreate, AnimeListRecommend, anime_detail
from anime import views


urlpatterns = [ 
    re_path('anime/.', AnimeListCreate.as_view()), #Paths everything after /anime to the Anime look up function
    path('anime/recommend/<str:title>', AnimeListRecommend.as_view(), name='recommend'), #Returns recommendations
    path('anime_id/<int:pk>', anime_detail, name='anime_id'), #Looks up anime_id
    ]


