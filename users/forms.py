from django.forms import forms

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']