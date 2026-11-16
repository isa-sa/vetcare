from django import forms
from .models import Tutor, Pet

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'cpf', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do tutor'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(71) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['tutor', 'nome', 'especie', 'raca', 'peso_kg', 'alergias']
        widgets = {
            'tutor': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do animal'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'raca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: SRD, Poodle, Siamês'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ex: 12.50'}),
            'alergias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Informe alergias conhecidas ou deixe em branco'}),
        }