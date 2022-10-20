from ast import Raise
from importlib.resources import contents
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from petville.models import UserData
from rest_framework import status
from .serializers import CurrentUserSerializer
from .serializers import LastLoginSerializer
from django.views.generic.detail import DetailView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests


class CurrentUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer

class LastLoginSerializer(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = LastLoginSerializer


class ServerStatus(viewsets.ViewSet):

    def list(self, request, format=None):
        #return Response(content, status=status.HTTP_200_OK)
        try:
            r = requests.get('http://127.0.0.1:8000/')
            content_err = {"status": "error", "code": "{}".format(r.status_code)}
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            pass
            return Response(content_err, status=status.HTTP_404_NOT_FOUND)
        else:
            content_ok = {"status": "OK", "code": "{}".format(r.status_code)}
            return Response(content_ok, status=status.HTTP_200_OK)



