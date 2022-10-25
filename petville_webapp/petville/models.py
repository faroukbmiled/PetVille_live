from random import choices
from urllib import request
import uuid
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from location_field.models.plain import PlainLocationField
from localflavor.tn.tn_governorates import GOVERNORATE_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


PER_CHOICES = (
    ("TND/day", "TND/day"),
    ("TND/hour", "TND/hour"),
)
MY_CHOICES = (('dogsitter', 'Dog sitter'),
              ('catsitter', 'Cat sitter'),
              ('petgrooming', 'Pet Grooming'),
              ('dogwalking', 'Dog Walking'),
              ('catwalking', 'Cat Walking'))
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=24, choices=GOVERNORATE_CHOICES, blank=True, null=True) 
    location = PlainLocationField(based_fields=['city','state'], zoom=7, null=True)
    per_what = models.CharField(max_length=11, choices=PER_CHOICES, null=True)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    my_field = models.CharField(max_length=500, choices=MY_CHOICES, null=True)
    
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
            

