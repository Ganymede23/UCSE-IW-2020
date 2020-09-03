from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


#este es el modelo de los escritos (no se si realmentte iria en la aplicacion usuarios o deberiamos pensar una nueva)
# (no se como decirle a los escritos en ingles xD)
#esto es lo que no esta migrando a la base de datos por mas que haga un "python manage.py migrate usuarios"

class Escrito(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default = datetime.datetime.now() )

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('escrito_details', args=(str(self.id)) )
        return reverse('homepage')
    