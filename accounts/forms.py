from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Patient


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Patient
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Patient
        fields = ('username', 'email')
