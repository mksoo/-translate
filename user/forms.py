from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    name = forms.CharField(label="이름")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "name", "email")

