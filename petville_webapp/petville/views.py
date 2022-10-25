from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.core import serializers
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
from .models import UserData, Profile
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, UpdateUserData


def home(request):
    return render(request, 'petville/home.html')

# def user_list(request):
#     data = serializers.serialize('json', User.objects.all())
#     return JsonResponse(data, safe=False)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'petville/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                state = form.cleaned_data.get('state')
                username = form.cleaned_data.get('username')
                city = form.cleaned_data.get('city')
                phone_number = form.cleaned_data.get('phone_number')
                location = form.cleaned_data.get('location')
                per_what = form.cleaned_data.get('per_what')
                cost = form.cleaned_data.get('cost')
                user = User.objects.get(username=username)
                user_data = UserData.objects.create(user=user, city=city, location=location, cost=cost,
                                                    state=state, phone_number=phone_number, per_what=per_what)
                user_data.save()
                profile = Profile.objects.create(user=user)
                profile.save()
                messages.success(request, 'Your account has been created successfully')
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, self.template_name, {'form': form})  
        


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'petville/password_reset.html'
    email_template_name = 'petville/password_reset_email.html'
    subject_template_name = 'petville/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('petville-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'petville/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('petville-home')
    
    
class UserListView(ListView):

    model = User
    template_name = 'petville/users.html'



def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_data = UpdateUserData(request.POST, request.FILES, instance=request.user.userdata)

        if user_form.is_valid() and profile_form.is_valid() and user_data.is_valid():
            user_form.save()
            profile_form.save()
            user_data.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='petville-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        user_data = UpdateUserData(instance=request.user.userdata)

    return render(request, 'petville/profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user_data': user_data})

def location(self, request, *args, **kwargs):
        if request.method == "POST":
            test = UpdateUserData(request.POST)
            if form.is_valid():
                form.save()
                latitude = form.cleaned_data.get('location')
                coor = form.cleaned_data.get('city')
                user = User.objects.get(username=user)
                user_data = UserData.objects.create(user=user, coor=coor, latitude=latitude)
                user_data.save()
                latt = UserData.objects.create(user=user)
                latt.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'petville/profile.html', {'test': test})  