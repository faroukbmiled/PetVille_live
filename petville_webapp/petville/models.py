from email.policy import default
from urllib import request
import uuid
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default='1')
    dogname = models.CharField(default='name', max_length=20)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userdata = models.OneToOneField(UserData, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='your bios here')

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (1024, 1024)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
            

