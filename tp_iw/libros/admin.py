from django.contrib import admin
from .models import Libro, Review, Rate, Comment_r

admin.site.register(Libro)
admin.site.register(Review)
admin.site.register(Rate)
admin.site.register(Comment_r)