from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Email
from .forms import FormEmailContato, FormEmailNovidades
from django.core.mail import send_mail


def home(request):
    form = FormEmailContato()
    form_email_novidades = FormEmailNovidades()
    if request.method == 'GET':
        return render(request, 'index.html', {'form': form, 'form_email_novidades':form_email_novidades})
    elif request.method == 'POST':
        return render(request, 'index.html', {'form': form,'form_email_novidades':form_email_novidades})

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

            send_mail(assunto, texto, 'caiocsilva97@gmail.com', [destinatario])
            
    return redirect('/')