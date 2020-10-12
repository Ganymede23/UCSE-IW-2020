from django.contrib import admin
from .models import  Comment, Denuncia, MotivoDenuncia

admin.site.register(Comment)
admin.site.register(Denuncia)
admin.site.register(MotivoDenuncia)