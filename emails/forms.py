from django import forms
from emails.models import EmailContato, Newslatter


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