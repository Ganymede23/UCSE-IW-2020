from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Libro(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    desc = RichTextField(blank=True, null=True)
    date_publish = models.DateTimeField(blank=True, null=True )
    portrait = models.ImageField(null= True, blank=True, upload_to="images/portrait")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Libro, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.date = timezone.now()
        self.save()  

    def get_detail_url(self): #devuelve url en home
        url = 'review_detail'
        return url

    def __str__(self):
        return self.title + ' | ' + str(self.author)



class Rate (models.Model): #modelo para ratear reviews
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.review.title) + ' | '+ str(self.usuario.username) + ' | ' + str(self.rating)

class Comment_r(models.Model):
    usuario_r = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    denuncias = models.ManyToManyField(User, related_name='comments_review')

    def total_denuncias(self):
        return self.denuncias.count()

    def __str__(self):
        return '%s - %s' % (self.review.title, self.usuario_r)

#motivos de las denuncias
class MotivoDenuncia_r(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo 

#denuncias
class Denuncia_r(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment_r, on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoDenuncia_r, on_delete=models.CASCADE)
    descripcion = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    aceptada = models.BooleanField(default=False)
    vista = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + ' | ' + str(self.motivo)