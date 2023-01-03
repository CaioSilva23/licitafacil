from django import forms
from .models import EmailContato, Email


class FormEmailContato(forms.ModelForm):
    
    class Meta:
        model = EmailContato
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-mail...', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto...', 'class': 'form-control'}),
            'texto': forms.Textarea(
                attrs={'placeholder': 'Digite sua mensagem...', 'rows':3, 'class': 'form-control'}),
        }


class FormEmailNovidades(forms.ModelForm):
    
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control', 'id':'email-input','placeholder':'Seu melhor e-mail'}),

        }