# movie_database_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),  # Include URLs from the 'movies' app
]