from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

from escritos.models import Escrito
from libros.models import Review

# Create your models here.
class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    escrito = models.ForeignKey(Escrito, related_name='comments_escrito', on_delete=models.CASCADE,  blank=True, null=True)
    review = models.ForeignKey(Review, related_name='comments_reviews',on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        if self.escrito is not None:
            return '%s - %s' % (self.escrito.title, self.usuario)
        else:
            return '%s - %s' % (self.review.title, self.usuario)

#motivos de las denuncias
class MotivoDenuncia(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo 

#denuncias
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