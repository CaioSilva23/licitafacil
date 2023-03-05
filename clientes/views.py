from django.shortcuts import render, redirect 
from clientes.forms import FormClientes
from django.contrib import messages


def cadastro(request):
    form = FormClientes(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')
    messages.success(request, 'Dados inválidos, tente novamente!')
    return redirect('home')