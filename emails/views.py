from django.shortcuts import render, redirect
from emails.forms import FormNewslatter, FormEmailContato
from django.contrib import messages
from emails.send_email import EnviaEmail





def newslatter(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        newslatter = FormNewslatter(request.POST)
        if newslatter.is_valid():
            newslatter.save()
            messages.success(request, 'Obrigado por se cadastrar!')
        else:
            messages.info(request, 'Email inválido!')
    return redirect('/')
        

def email_contato(request):
    if request.method =='GET':
        return redirect('/')
    elif request.method == 'POST':
        form_contato = FormEmailContato(request.POST)
        if form_contato.is_valid():
            form_contato.save()

            # email = EnviaEmail(form_contato)
            
            # email.confirmacao_contato_plataforma()
            # email.confirmacao_contato_usuario()


            messages.success(request, 'Recebemos a sua mensagem, em breve entraremos em contato!')
    return redirect('/')