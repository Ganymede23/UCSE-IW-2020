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
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Libro, on_delete=models.CASCADE)
    rate = models.FloatField()
    desc = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    date = models.DateTimeField(blank=True, null=True )


    def publish(self):
        self.date = timezone.now()
        self.save()    

    def __str__(self):
        return self.title + ' | ' + str(self.author)