from django.contrib import admin
from django.urls import path, include, re_path

from .escritos_views import escritodetail

urlpatterns = [
    path('escrito_details/<int:pk>', escritodetail, name= 'escritos_details')
]
