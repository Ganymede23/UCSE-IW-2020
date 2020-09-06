from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime


#este es el modelo de los escritos 

class Escrito(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default = datetime.datetime.now() )

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('escritos_details', args=(str(self.id)) )
        return reverse('homepage')