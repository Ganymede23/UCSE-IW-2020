from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
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


    def publish(self): #cambia el datetime de publicacion cuando se clickea en publicar 
        self.date = timezone.now()
        self.save()    
    
    def get_detail_url(self): #devuelve url en home
        url = 'escrito_detail'
        return url

    def __str__(self):
        return self.title + ' | ' + str(self.author)


#modelo de comenntarios
class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    escrito = models.ForeignKey(Escrito, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.escrito.title, self.usuario)


class MotivoDenuncia(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo 


class Denuncia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoDenuncia, on_delete=models.CASCADE)
    descripcion = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    aceptada = models.BooleanField(default=False)
    vista = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + ' | ' + str(self.motivo)



