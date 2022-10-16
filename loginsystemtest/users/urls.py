from django.urls import path
from .views import home, profile, RegisterView
from users import views
from django.urls import include, path
from users import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
