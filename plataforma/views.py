from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plataforma
from .forms import FormEmailContato, FormEmailNovidades
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    plataforma = Plataforma.objects.get(id=1) 

    form = FormEmailContato()
    form_email_novidades = FormEmailNovidades()

    context = {
                'form': form,
                 'form_email_novidades':form_email_novidades,
                  'plataforma': plataforma
                }

    if request.method == 'GET':
        return render(request, 'index.html', context )
    elif request.method == 'POST':
        return render(request, 'index.html', {'form': form,'form_email_novidades':form_email_novidades,'plataforma': plataforma})

def email(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        email_novidade = FormEmailNovidades(request.POST)
        if email_novidade.is_valid():
            email_novidade.save()
    return redirect('/')
        

def contato(request):
    if request.method =='GET':
        return redirect('/')
    elif request.method == 'POST':
        contato = FormEmailContato(request.POST)
        if contato.is_valid():
            contato.save()

            destinatario = contato.cleaned_data['email']
            assunto = contato.cleaned_data['assunto']
            texto = contato.cleaned_data['texto']

            send_mail(assunto, f'O usuário, {destinatario} deixou uma mensagem abaixo:\n\n{texto}', settings.DEFAULT_FROM_EMAIL, ['contatolicitafacilbr@gmail.com'])
            send_mail('Licita Facil BR', f'Olá, recebemos a sua mensagem, em breve entraremos em contato.', settings.DEFAULT_FROM_EMAIL, [destinatario])
            
            
    return redirect('/')