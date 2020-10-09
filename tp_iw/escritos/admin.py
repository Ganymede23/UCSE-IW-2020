from django.contrib import admin
from .models import Escrito, Comment, Denuncia, MotivoDenuncia

admin.site.register(Escrito)
admin.site.register(Comment)
admin.site.register(Denuncia)
admin.site.register(MotivoDenuncia)
