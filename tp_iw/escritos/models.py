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
    likes = models.ManyToManyField(User, related_name='post_escritos')

    def total_likes(self):
        return self.likes.count()


    def publish(self):
        self.date = timezone.now()
        self.save()    
    
    def get_detail_url(self): #devuelve url en home
        url = 'escrito_detail'
        return url

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    escrito = models.ForeignKey(Escrito, related_name='comments', on_delete=models.CASCADE)
    denuncias = models.ManyToManyField(User, related_name='comments_escritos')

    def total_denuncias(self):
        return self.denuncias.count()

    def __str__(self):
        return '%s - %s' % (self.escrito.title, self.usuario)



