from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_pic = profile_pic = models.ImageField(null= True, blank=True, upload_to="images/profiles")
    following = models.ManyToManyField(User, related_name='following', blank=True)
    
    def profiles_usuario(self):
        return self.user
    
    def __str__(self):
        return str(self.user)