from django.urls import path
from .views import home, profile, RegisterView, CustomLoginView
from petville import views
from django.urls import include, path
from petville import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', home, name='petville-home'),
    path('register/', RegisterView.as_view(), name='petville-register'),
    path('profile/', profile, name='petville-profile'),
    path('about/', CustomLoginView.as_view( template_name='petville/about.html'), name='about'),
]
