from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone


#este es el modelo de los escritos 

class Escrito(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    date = models.DateTimeField(blank=True, null=True )


    def publish(self):
        self.date = timezone.now()
        self.save()    
    
    def get_detail_url(self): #devuelve url en home
        url = 'escrito_detail'
        return url

    def __str__(self):
        return self.title + ' | ' + str(self.author)


