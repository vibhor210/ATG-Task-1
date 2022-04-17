from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}),max_length=32)
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    image = forms.ImageField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","image","first_name","last_name","email","password1","password2")