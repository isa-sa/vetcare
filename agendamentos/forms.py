from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['pet', 'veterinario', 'data_hora', 'motivo']
        widgets = {
            'pet': forms.Select(attrs={'class': 'form-select'}),
            'veterinario': forms.Select(attrs={'class': 'form-select'}),
            'data_hora': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'motivo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ex: Vacinação anual, consulta de rotina, emergência'}
            ),
        }