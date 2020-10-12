from django.urls import path, include
from .escritos_views import escrito_remove,escrito_publish, escrito_detail, escrito_new, escrito_edit, like_escrito, escrito_leido

urlpatterns = [
    path('escrito_details/<int:pk>', escrito_detail, name = 'escrito_detail'),
    path('add_escrito', escrito_new, name = 'add_escrito'),   
    path('escrito/<pk>/remove/', escrito_remove, name='escrito_remove'),
    path('escrito/<pk>/publish/', escrito_publish, name='escrito_publish'),
    path('escrito/<int:pk>/edit/', escrito_edit, name='edit_escrito'),
    path('like/<int:pk>', like_escrito, name='escrito_like'),
    path('escrito_leido/', escrito_leido, name='escrito_leido'),
    path('search/', include('haystack.urls')),
]

