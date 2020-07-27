#from django.conf.urls import url
from . import views
#from django.contrib import admin
from django.urls import path #include와 urls를 사용하기위해 import 해줘야 하는것

urlpatterns = [
    path('go', views.go_game, name='go_game'),
    path('', views.game_list, name='game_list'),
]
