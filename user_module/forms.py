from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'username', 'placeholder': 'username'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'phone', 'placeholder': 'phone'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password', 'placeholder': 'password', 'autocomplete': 'off'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password', 'placeholder': 'password(repeat)', 'autocomplete': 'off'
    }))

    class Meta:
        model = UserModel
        fields = ('username', 'phone', 'password1', 'password2')


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'username', 'placeholder': 'username or phone'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password', 'placeholder': 'password', 'autocomplete': 'off'
    }))


class ForgetPassForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'phone', 'placeholder': 'phone'
    }))


class ChangePassForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password', 'placeholder': 'password', 'autocomplete': 'off'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password', 'placeholder': 'password(repeat)', 'autocomplete': 'off'
    }))

    class Meta:
        model = UserModel
        fields = ('password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'phone')
