from ast import Raise
from importlib.resources import contents
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import status
from .serializers import CurrentUserSerializer
from .serializers import LastLoginSerializer
from django.views.generic.detail import DetailView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.test import APITestCase
from rest_framework.response import Response
import requests


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer

class LastLoginSerializer(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = LastLoginSerializer


class ServerStatus(viewsets.ViewSet):

    def list(self, request, format=None):
        
        content_ok = {"status": "OK", "code": "200"}
        #return Response(content, status=status.HTTP_200_OK)
        try:
            r = requests.get('http://127.0.0.1:8000/')
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            content_err = {"status": "error", "code": {r.status_code}}
            pass
            return Response(content_err, status=status.HTTP_404_NOT_FOUND)
        
        return Response(content_ok, status=status.HTTP_200_OK)



