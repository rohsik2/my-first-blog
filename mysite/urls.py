from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls')),
    path('games/', include('games.urls')),
    path('', include('army_vacation.urls')),
]
