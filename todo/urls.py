#from django.conf.urls import url
from . import views
#from django.contrib import admin
from django.urls import path #include와 urls를 사용하기위해 import 해줘야 하는것

urlpatterns = [
    path('', views.bucket_list, name='bucket_list'),
    path('<int:pk>/', views.bucket_detail, name='bucket_detail'),
    path('new/', views.bucket_new, name='bucket_new'),
    path('<int:pk>/edit/', views.bucket_edit, name='bucket_edit'),
]
