from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, UserData
from location_field.forms.plain import PlainLocationField
from localflavor.tn.forms import TNGovernorateSelect
from localflavor.tn.tn_governorates import GOVERNORATE_CHOICES
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from django.core.validators import MaxLengthValidator

PER_CHOICES = (
    ("TND/day", "TND/day"),
    ("TND/hour", "TND/hour"),
)
MY_CHOICES = (('dogsitter', 'Dog sitter'),
              ('catsitter', 'Cat sitter'),
              ('petgrooming', 'Pet Grooming'),
              ('dogwalking', 'Dog Walking'),
              ('catwalking', 'Cat Walking'))



blank_choice = (('', '-- Select state --'),)
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=15,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=15,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=10,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control', 'id': 'usnm',
                                                             }))
    email = forms.EmailField(max_length=30, required=True,
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
                                                                  'id': 'password','id': 'password2',
                                                                  }))
    city = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Your Adress','class': 'form-control'}))
    state = forms.ChoiceField(choices=blank_choice+GOVERNORATE_CHOICES, required=True,
                              widget=forms.Select(attrs={'class':'form-dropdown form-control'}))
    
    per_what = forms.ChoiceField(choices=PER_CHOICES, required=True,
                              widget=forms.Select(attrs={'class':'form-dropdown form-control'}))
    
    
    location = PlainLocationField(max_length=10,attrs={'style': 'position: absolute;left: -999em;'}, based_fields=['city', 'state'],
                                  initial='36.80105674280464, 10.181972264198441')
    
    cost = forms.DecimalField(max_digits=4, decimal_places=2, required=True,
                              widget=forms.TextInput(attrs={'placeholder': "Starting rate",'class': 'form-control',
                                                                  }))
    
    phone_number = PhoneNumberField(region="TN", min_length=8, max_length=12, 
                              widget=RegionalPhoneNumberWidget(attrs={'placeholder': "Phone Number: +216...",'class': 'form-control',
                                                                  }))
    my_field = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-dropdown form-control checkboxclass'}),
                                          choices=MY_CHOICES)
    
    questions = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'placeholder': "Answer these questions here...",
                                                             'class': 'form-control', 'rows': 5}))
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'city', 
                  'state', 'location', 'phone_number', 'per_what', 'cost', 'my_field', 'questions']


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
    first_name = forms.CharField(max_length=15,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=15,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'style': 'position: absolute;left: -999em;','class': '', 'id': 'imageupload'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
class UpdateUserData(forms.ModelForm):
    city = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = PlainLocationField(attrs={'style': 'position: absolute;left: -999em;'}, based_fields=['city', 'state'],
                                  initial='36.80105674280464, 10.181972264198441')
    state = forms.ChoiceField(choices=blank_choice+GOVERNORATE_CHOICES, required=True, 
                              widget=forms.Select(attrs={'class':'form-dropdown form-control'}))
    per_what = forms.ChoiceField(choices=PER_CHOICES, required=True,
                              widget=forms.Select(attrs={'class':'form-dropdown form-control'}))
    
    cost = forms.DecimalField(max_digits=4, decimal_places=2, required=True,
                              widget=forms.TextInput(attrs={'placeholder': "Starting rate",'class': 'form-control',
                                                                  }))
    
    phone_number = PhoneNumberField(region="TN", min_length=8, max_length=12, 
                              widget=RegionalPhoneNumberWidget(attrs={'placeholder': "Phone Number: +216...",'class': 'form-control',
                                                                  }))
    my_field = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-dropdown form-control checkboxclass'}),
                                          choices=MY_CHOICES)
    
    questions = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'placeholder': "Answer these questions here...",
                                                             'class': 'form-control', 'rows': 5}))
    
    class Meta:
        model = UserData
        fields = ['location', 'city', 'state', 'per_what', 'cost', 'phone_number', 'my_field', 'questions']
        
        
class ClassMap(forms.ModelForm):
    cityuser = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'style': 'position: absolute;left: -999em;'}))
    location = PlainLocationField(attrs={'style': 'position: absolute;left: -999em;'}, based_fields=['city', 'state'],
                                  initial='36.80105674280464, 10.181972264198441')
    
    class Meta:
        model = UserData
        fields = ['cityuser', 'location']
        
        