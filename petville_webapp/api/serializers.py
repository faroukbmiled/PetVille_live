from enum import auto
from django.contrib.auth.models import User, Group
from petville.models import UserData, Profile
from django.db import models
from rest_framework import serializers
from rest_framework import status
from drf_writable_nested import WritableNestedModelSerializer


class ProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'avatar',)


class UserDataSerializer(serializers.ModelSerializer):
    dogname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = UserData
        fields = ('id', 'dogname', 'age',)

class CurrentUserSerializer(WritableNestedModelSerializer):
    
    profile = ProfileSerializer()
    userdata = UserDataSerializer()
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'userdata', 'profile',)
        
class LastLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')
