from django.contrib import admin
from .models import Libro, Review, Rate

admin.site.register(Libro)
admin.site.register(Review)
admin.site.register(Rate)