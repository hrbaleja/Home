from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer,Topic,ourservice
from bootstrap_datepicker_plus.widgets import DatePickerInput




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
    fields = "__all__"

class Customerform(forms.ModelForm):
    First_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name',  'class': 'form__field form__text', }))
    Last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name',  'class': 'form__field form__text'}))
    Address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Address',  'class': 'form__field form__text'}))
    DOB = forms.DateField(widget=forms.DateInput( 
        attrs={'placeholder': 'Date Of Birth',  'class': 'form__field form__text'}))
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',  'class': 'form__field form__text'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',  'class': 'form__field form__text'}))
    Contact = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Contact',  'class': 'form__field form__text'}))
   
    class Meta:
        model = Customer
        fields ="__all__"

class Topicform(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter New Topic',  'class': 'form__field form__text', }))

    class Meta:
        model = Topic
        fields ="__all__"
class ourserviceform(forms.ModelForm):    
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Title',  'class': 'form__field form__text', }))
    people = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'People',  'class': 'form__field form__text', }))
    discount = forms.CharField(widget=forms.NumberInput(
         attrs={'placeholder': 'Discount Price',  'class': 'form__field form__text', }))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Price',  'class': 'form__field form__text', }))
    lista = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Features',  'class': 'form__field form__text', }))
    listb = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Features',  'class': 'form__field form__text', }))
    listc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Features',  'class': 'form__field form__text', }))
    listd = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Features',  'class': 'form__field form__text', }))
    liste = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Features',  'class': 'form__field form__text', }))

   
    class Meta:
        model = ourservice
        fields ="__all__"