from django import forms
from .models import EmailContato


class FormEmailContato(forms.ModelForm):
    
    class Meta:
        model = EmailContato
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-mail...'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto...'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto...'}),
            'texto': forms.Textarea(
                attrs={'placeholder': 'Digite sua mensagem...', 'rows':3}),
        }