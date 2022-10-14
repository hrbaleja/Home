
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',  'class': 'form__field form__text', }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name',  'class': 'form__field form__text'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name',  'class': 'form__field form__text'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address',  'class': 'form__field form__text'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',  'class': 'form__field form__text'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password',  'class': 'form__field form__text'}))


class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name',
              'email', 'password1', 'password2', ]
