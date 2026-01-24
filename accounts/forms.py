from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Informe um email válido."
        }
    )

    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        error_messages={
            "required": "A senha é obrigatória."
        }
    )

    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput,
        error_messages={
            "required": "Confirme sua senha."
        }
    )
