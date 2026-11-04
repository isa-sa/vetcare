from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório para recuperar a senha.")

    class Meta:
        model = User
        fields = ['username', 'email']