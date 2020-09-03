from django.contrib import admin
from django.urls import path, include, re_path

from .escritos_views import Escrito_Detail_View,add_escrito_view

urlpatterns = [
    path('escrito_details/<int:pk>', Escrito_Detail_View.as_view(), name = 'escritos_details'),
    path('add_escrito', add_escrito_view.as_view(), name = 'add_escrito')
]
