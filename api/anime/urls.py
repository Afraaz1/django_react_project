from anime import views 
from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/anime/', views.AnimeListCreate.as_view()),
]
