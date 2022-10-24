from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, UserData
from location_field.forms.plain import PlainLocationField
from localflavor.tn.forms import TNGovernorateSelect
from localflavor.tn.tn_governorates import GOVERNORATE_CHOICES

blank_choice = (('', '-- Select state --'),)
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    age = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': "Dog's age",
                                                                  'class': 'form-control',
                                                                  }))
    dogname = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Dog Name',
                                                                  'class': 'form-control',
                                                                  }))
    city = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Your Adress','class': 'form-control'}))
    state = forms.ChoiceField(choices=blank_choice+GOVERNORATE_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-dropdown form-control'}))
    
    location = PlainLocationField(attrs={'style': 'position: absolute;left: -999em;'}, based_fields=['city', 'state'],
                                  initial='36.80105674280464, 10.181972264198441')
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age', 'dogname', 'city', 'state', 'location',]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
class UpdateUserData(forms.ModelForm):
    age = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    dogname = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = PlainLocationField(attrs={'style': 'position: absolute;left: -999em;'}, based_fields=['city'],
                                  initial='36.80105674280464, 10.181972264198441')
    state = TNGovernorateSelect(attrs={'class': 'form-control'})
    
    
    class Meta:
        model = UserData
        fields = ['age', 'dogname','location', 'city', 'state']
        