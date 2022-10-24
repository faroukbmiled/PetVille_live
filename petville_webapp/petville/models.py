from random import choices
from urllib import request
import uuid
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from location_field.models.plain import PlainLocationField
from localflavor.tn.tn_governorates import GOVERNORATE_CHOICES  


# Extending User Model Using a One-To-One Link

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default='1')
    dogname = models.CharField(default='name', max_length=20)
    city = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True)
    state = models.CharField(max_length=24, choices=GOVERNORATE_CHOICES, blank=True, null=True)  
    
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
            

