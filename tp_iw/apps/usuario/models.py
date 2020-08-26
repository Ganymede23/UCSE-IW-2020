from django.db import models

# Create your models here.

class Escrito(models.Model):
    
    titulo = models.CharField( max_length=50)
    cuerpo = models.CharField( max_length=50)
    # autor = models.ForeignKey("app.model", verbose_name=_(""), on_delete=models.CASCADE)  # llamar a la  clase user en el app.model      
