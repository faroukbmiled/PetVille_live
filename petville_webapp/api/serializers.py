from enum import auto
from django.contrib.auth.models import User, Group
from petville.models import UserData, Profile
from django.db import models
from rest_framework import serializers
from rest_framework import status
from drf_writable_nested import WritableNestedModelSerializer

MY_CHOICES = (('dogsitter', 'Dog sitter'),
              ('catsitter', 'Cat sitter'),
              ('petgrooming', 'Pet Grooming'),
              ('dogwalking', 'Dog Walking'),
              ('catwalking', 'Cat Walking'))
PER_CHOICES = (
    ("TND/day", "TND/day"),
    ("TND/hour", "TND/hour"),
)

class ProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'avatar',)


class UserDataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False) 
    location = serializers.CharField(required=False)
    per_what = serializers.ChoiceField(required=False, choices=PER_CHOICES)
    cost = serializers.DecimalField(required=False, max_digits=13, decimal_places=4)
    phone_number = serializers.CharField(required=False)
    my_field = serializers.ChoiceField(required=False, choices=MY_CHOICES)
    questions = serializers.CharField(required=False)
    class Meta:
        model = UserData
        fields = ('id', 'city', 'state', 'location', 'per_what', 'cost',
                  'phone_number', 'my_field', 'questions')

class CurrentUserSerializer(WritableNestedModelSerializer):
    
    profile = ProfileSerializer()
    userdata = UserDataSerializer()
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'userdata', 'profile',)
        
class LastLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')
