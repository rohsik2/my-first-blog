# from django.conf.urls import url
from . import views
# from django.contrib import admin
from django.urls import path  # include와 urls를 사용하기위해 import 해줘야 하는것


urlpatterns = [
    path('', views.main_menu, name='main_menu'),
]
