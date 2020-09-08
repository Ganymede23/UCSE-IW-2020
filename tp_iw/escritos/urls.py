from django.contrib import admin
from django.urls import path, include, re_path

from .escritos_views import  escritos_draft_list, escrito_remove,escrito_publish, escrito_detail, escrito_new, escrito_edit

urlpatterns = [
    path('escrito_details/<int:pk>', escrito_detail, name = 'escrito_detail'),
    path('add_escrito', escrito_new, name = 'add_escrito'),
    path('drafts/', escritos_draft_list, name='escritos_draft_list'),
    path('escrito/<pk>/remove/', escrito_remove, name='escrito_remove'),
    path('escrito/<pk>/publish/', escrito_publish, name='escrito_publish'),
    path('escrito/<int:pk>/edit/', escrito_edit, name='edit_escrito'),
]

