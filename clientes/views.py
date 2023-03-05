from django.shortcuts import redirect 
from clientes.forms import FormClientes, FormEmailContato, FormNewslatter
from django.contrib import messages


def cadastro(request):
    form = FormClientes(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastro realizado com sucesso, você receberá em breve por email o link para pagamento.')
        return redirect('home')
    messages.success(request, 'Dados inválidos, tente novamente!')
    return redirect('home')


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
            messages.success(request, 'Recebemos a sua mensagem, em breve entraremos em contato!')
    return redirect('/')