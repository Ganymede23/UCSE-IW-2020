from django.contrib import admin
from django.urls import path, include

from .libros_views import show_books,book_detail

urlpatterns = [
    path('show_books/', show_books, name='show_books'),
    path('book_details/<int:pk>', book_detail, name = 'book_detail'),
]