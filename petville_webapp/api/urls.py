from django.urls import path
from petville.views import home, profile, RegisterView
from api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.CurrentUserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
