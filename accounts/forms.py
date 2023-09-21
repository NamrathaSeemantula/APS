from email.policy import default
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your username here'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your first name here'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your last name here'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your email here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your password here'}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

DEPT_CHOICES = [
    ('Bio Medical Engineering', 'Bio Medical Engineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
    ('Electrical and Communications Engineering', 'Electrical and Communications Engineering'),
    ('Information Technology', 'Information Technology'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
]

class UserProfileInfoForm(forms.ModelForm):
    dept = forms.CharField(label='Department', widget=forms.Select(choices=DEPT_CHOICES, attrs={'class': 'input-fields'}))
    passed_out_year = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-fields', 'placeholder': 'Enter your passed out year here'}))
    class Meta():
        model = UserProfileInfo
        fields = ('passed_out_year', 'dept', 'profile_pic',)