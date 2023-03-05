from django import forms
from clientes.models import Cliente

class FormClientes(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'id-email-cadastro'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control telefone'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            }
        