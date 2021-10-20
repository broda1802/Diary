from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#         form = 'form.html'
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#

class AddUserAndPatientForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

