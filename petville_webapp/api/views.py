from importlib.resources import contents
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import status
from .serializers import CurrentUserSerializer
from .serializers import LastLoginSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.test import APITestCase
from rest_framework.response import Response
from http import HTTPStatus
from django.http import HttpResponse
from requests import get
from django.test import TestCase
import json


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer

class LastLoginSerializer(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = LastLoginSerializer


class IndexTests(APIView):
    def test_success(self, request):
        return ("test")

