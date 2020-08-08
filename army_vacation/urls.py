# from django.conf.urls import url
from . import views
# from django.contrib import admin
from django.urls import path 


urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('apply_vacation', views.apply_vacation, name='apply_vacation'),
    path('questionaire', views.questionaire, name='questionaire'),
    path('login', views.login, name='login'),
    path('handbook', views.handbook, name='handbook'),
    path('food/<int:month_date>', views.food, name='food'),
    path('vacation_list', views.vacation_list, name='vacation_list'),
]
