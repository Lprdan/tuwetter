from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Email é obrigatório.",
            "invalid": "Digite um email válido.",
        }
    )

    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        error_messages={
            "required": "Senha é obrigatória.",
        },
        help_text="Mínimo 8 caracteres."
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput,
        error_messages={
            "required": "Confirme sua senha.",
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("As senhas não conferem.")
            if len(password1) < 8:
                raise forms.ValidationError("A senha deve ter no mínimo 8 caracteres.")

        return password2
