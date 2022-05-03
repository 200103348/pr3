from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Logreg(forms.ModelForm):
    class Meta:
        model = regis
        fields = ['username', 'f_name', 'l_name', 'age', 'email', 'password', 'confirm', 'gender']


'''class CreateUserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']'''