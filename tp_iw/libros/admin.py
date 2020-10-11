from django.contrib import admin
from .models import Libro, Review, Rate, Comment_r, Denuncia_r, MotivoDenuncia_r

admin.site.register(Libro)
admin.site.register(Review)
admin.site.register(Rate)
admin.site.register(Comment_r)
admin.site.register(Denuncia_r)
admin.site.register(MotivoDenuncia_r)