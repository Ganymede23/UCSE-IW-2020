from django.contrib import admin
from django.urls import path, include

from .libros_views import (show_books, book_detail, review_new, review_edit,
review_publish, review_remove, review_detail, delete_comment, denuncia_comment)

urlpatterns = [
    path('show_books/', show_books, name='show_books'),
    path('book_detail/<int:pk>', book_detail, name = 'book_detail'),

    path('add_review/<int:pk_libro>', review_new, name = 'add_review'),
    path('review_detail/<int:pk>', review_detail, name = 'review_detail'),
    path('review/<pk>/remove/', review_remove, name='review_remove'),
    path('review/<pk>/publish/', review_publish, name='review_publish'),
    path('review/<int:pk>/edit/', review_edit, name='edit_review'),


    path('comment/<int:pk>/delete/', delete_comment, name='comment_delete'),
    path('comment/<int:pk>/denuncia/', denuncia_comment, name='comment_denuncia'),
]