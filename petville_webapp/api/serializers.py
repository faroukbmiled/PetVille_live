from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from petville.models import UserData
from django.db import models
from rest_framework import serializers
from rest_framework import status


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('age')

class CurrentUserSerializer(serializers.ModelSerializer):
    
    agee = serializers.CharField(source = 'userdata.age', read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'agee')
        
class LastLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')
