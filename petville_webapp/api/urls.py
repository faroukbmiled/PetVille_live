from django.urls import path
from petville.views import home, RegisterView
from .views import LastLoginSerializer, CurrentUserViewSet, ServerStatus
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', CurrentUserViewSet, 'users')
router.register(r'login', LastLoginSerializer, 'last_login')
router.register(r'status', ServerStatus, 'status')

urlpatterns = [
    path(r'api/v1/', include(router.urls)),
]
