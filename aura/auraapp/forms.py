# forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'senha']
