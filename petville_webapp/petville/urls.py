from django.urls import path
from .views import home, RegisterView, CustomLoginView, profile, UserListView, user_info,homepage
from petville import views
from django.urls import include, path
from petville import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', homepage, name='petville-home'),
    path('register/', RegisterView.as_view(), name='petville-register'),
    path('profile/', profile, name='petville-profile'),
    path('petsitter/id/<int:pk>/', views.user_info, name='profile_pk'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('find/', UserListView.as_view( template_name='petville/find.html'), name='find'),
    path('about/', CustomLoginView.as_view( template_name='petville/about.html'), name='about'),
    path('vet/', CustomLoginView.as_view( template_name='petville/vet.html'), name='vet'),
    path('gallery/', CustomLoginView.as_view( template_name='petville/gallery.html'), name='gallery'),
]
