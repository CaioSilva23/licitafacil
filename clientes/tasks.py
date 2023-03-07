from celery import shared_task 
from django.conf import settings
from clientes.models import Cliente, EmailContato
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import Http404
from django.shortcuts import get_object_or_404

@shared_task
def cadastro_email(id):
    model = get_object_or_404(Cliente, id=id)
    context = {
    'nome': model.nome,
    'telefone': model.telefone,
    'email': model.email,
    'servico': model.servico
    }

    html_content = render_to_string('email/email_cadastro.html', context=context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject='Cadastro realizado - Licita Facil BR', body=text_content, to=[model.email])
    email.attach_alternative(html_content, 'text/html')
    email.send()


    html_content2 = render_to_string('email/email_confirm_plataforma.html', context=context)
    text_content2 = strip_tags(html_content2)
    email2 = EmailMultiAlternatives(subject=f'Novo cadastro - Usuário {model.nome}', body=text_content2, to=[settings.DEFAULT_FROM_EMAIL])
    email2.attach_alternative(html_content, 'text/html')
    email2.send()
        
    if email.send and email2.send:
        return 1
    else:
        raise Http404


class EnviaEmailContato:

    def __init__(self, cliente: EmailContato):
        self.__model = cliente

    def mail_contato(self):
        context = {
        'email': self.__model.email,
        'assunto': self.__model.assunto,
        'texto':self.__model.texto,
        }

        html_content = render_to_string('email/email.html', context=context)

        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject='Licita Facil BR', body=text_content, to=[self.__model.email])
        email.attach_alternative(html_content, 'text/html')
        email.send()
            

        # EMAIL DE AVISO PARA A PLATAFORMA
        html_content2 = render_to_string('email/email_plataforma.html', context=context)
        text_content2 = strip_tags(html_content2)
        
        email2 = EmailMultiAlternatives(subject=f'Assunto: {self.__model.assunto}', body=text_content2, to=[settings.DEFAULT_FROM_EMAIL])
        email2.attach_alternative(html_content, 'text/html')
        email2.send()

        if email.send and email2.send:
            return 1
        else:
            raise Http404