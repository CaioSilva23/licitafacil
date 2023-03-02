from django.shortcuts import render, redirect
from .models import Plataforma
from emails.forms import FormNewslatter, FormEmailContato
from plataforma.models import Secao1, Card, Secao4



def home(request):
    plataforma = Plataforma.objects.all().first()

    # SECOES
    secao1 = Secao1.objects.all().first()
    cards = Card.objects.all()
    secao4 = Secao4.objects.all().first()
   
 
    form = FormEmailContato()
    form_email_novidades = FormNewslatter()

    context = {
                'form': form,
                'form_email_novidades':form_email_novidades,
                'plataforma': plataforma,

                ## SECOES
                'secao1': secao1,
                'cards': cards,
                'secao4': secao4
                
                }

    if request.method == 'GET':
        return render(request, 'index.html', context )
    elif request.method == 'POST':
        return render(request, 'index.html', context)
    