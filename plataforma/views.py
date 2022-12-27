from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Email
from .forms import FormEmailContato

def home(request):
    form = FormEmailContato()
    if request.method == 'GET':
        return render(request, 'index.html', {'form': form})
    elif request.method == 'POST':
        return render(request, 'index.html', {'form': form})



def email(request):
    if request.method == 'GET':
        return redirect('/home/')
    elif request.method == 'POST':
        email = request.POST.get('email_novidades')
        buscar_email = Email.objects.filter(email=email)

        if not buscar_email:
            if len(email) != 0:
                novo_email = Email(email = email)
                novo_email.save()
            print(email)
    return redirect('/home/')
        

def contato(request):
    if request.method =='GET':
        return redirect('/home/')
    elif request.method == 'POST':
        contato = FormEmailContato(request.POST)
        if contato.is_valid():
            contato.save()
            print('salvo')
    return redirect('/home/')