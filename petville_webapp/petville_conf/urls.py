from django.contrib import admin

from django.urls import path, include
from django.urls import include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from petville.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from rest_framework import routers
from petville import views
from api import views

from petville.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('petville.urls')),

    path('', include('api.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='petville/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('test/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='petville/loginbb.html',
                                           authentication_form=LoginForm), name='test'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='petville/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='petville/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
