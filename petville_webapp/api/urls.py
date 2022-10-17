from django.urls import path
from petville.views import home, profile, RegisterView
from .views import LastLoginSerializer, CurrentUserViewSet, IndexTests
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', CurrentUserViewSet, 'users')
router.register(r'login', LastLoginSerializer, 'last_login')


urlpatterns = [
    path(r'api/v1/', include(router.urls)),
    path('status/', IndexTests.as_view()),
]
