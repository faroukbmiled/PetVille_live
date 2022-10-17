from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import status


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

class LastLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


        
