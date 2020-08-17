from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('login', views.UserLoginView.as_view(), name='login'),

]