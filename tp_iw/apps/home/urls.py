from django.contrib import admin
from django.urls import path

from .home_views import index, home_page

urlpatterns = [
    path('', index, name='index'),
    path('index/', index),
    path('homepage/', home_page, name='homepage'),
]
