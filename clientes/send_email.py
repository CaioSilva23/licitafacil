from django.conf import settings
from clientes.models import Cliente

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404

class EnviaEmail:

    def __init__(self, cliente: Cliente):
        self.__nome = cliente.nome
        self.__email = cliente.email
        self.__telefone = cliente.telefone
        self.__servico = cliente.servico

    def cadastro_email(self):
        context = {
        'nome': self.__nome,
        'telefone': self.__telefone,
        'email':self.__email,
        'servico':self.__servico
        }

        # EMAIL PARA O USUÁRIO
        # RENDERIZA O TEMPLATE HTML
        html_content = render_to_string('email/email_cadastro.html', context=context)
        # RETIRA AS TAGS HTML
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject='Cadastro realizado - Licita Facil BR', body=text_content, to=[self.__email])
        email.attach_alternative(html_content, 'text/html')
        email.send()
            


        if email.send():
            return 1
        else:
            raise Http404

