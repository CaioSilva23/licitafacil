from django.core.mail import send_mail
from django.conf import settings
from .models import EmailContato
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404

class EnviaEmail:

    def __init__(self, email: EmailContato):
        self.__email = email

    def mail_contato(self):
        context = {
        'email': self.__email.email,
        'assunto': self.__email.assunto,
        'texto':self.__email.texto,
        }

        # EMAIL PARA O USUÁRIO
        # RENDERIZA O TEMPLATE HTML
        html_content = render_to_string('email/email.html', context=context)
        # RETIRA AS TAGS HTML
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject='Licita Facil BR', body=text_content, to=[self.__email.email])
        email.attach_alternative(html_content, 'text/html')
        email.send()
            

        # EMAIL DE AVISO PARA A PLATAFORMA
        html_content2 = render_to_string('email/email_plataforma.html', context=context)
        text_content2 = strip_tags(html_content2)
        
        email2 = EmailMultiAlternatives(subject=f'Assunto: {self.__email.assunto}', body=text_content2, to=[settings.DEFAULT_FROM_EMAIL])
        email2.attach_alternative(html_content, 'text/html')
        email2.send()

        if email.send() and email2.send():
            return 1
        else:
            raise Http404

