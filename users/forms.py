from django import forms

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name")
