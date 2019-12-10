from django.contrib import admin
from django.urls import path, include #include와 urls를 사용하기위해 import 해줘야 하는것


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('todo/', include('todo.urls')),
]
