from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.safestring import mark_safe

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "name": "email-username",
                "placeholder": "Insira seu username", 
                "autofocus": True,

            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "name": "password",
                "placeholder": mark_safe("&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;"),
                "aria-describedby": "password",
            }
        )
    )