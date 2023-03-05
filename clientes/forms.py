from django import forms
from clientes.models import Cliente, Newslatter, EmailContato

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
        

class FormEmailContato(forms.ModelForm):
    class Meta:
        model = EmailContato
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail...','id':'id_email', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto...','id':'id_assunto', 'class': 'form-control'}),
            'texto': forms.Textarea(
                attrs={'placeholder': 'Digite sua mensagem...', 'rows':3,'id':'id_texto', 'class': 'form-control'}),
        }


class FormNewslatter(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'email-input','placeholder':'Seu melhor e-mail'}),
            
        }