from django.urls import path
from users.views import home, profile, RegisterView
from api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'admin', views.CurrentUserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
]
