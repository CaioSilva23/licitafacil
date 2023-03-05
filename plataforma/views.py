from django.shortcuts import render
from emails.forms import FormNewslatter, FormEmailContato
from plataforma.models import Secao1, Secao4, Secao2, Secao3, Secao5
from clientes.forms import FormClientes



def home(request):
    # SECOES
    secao1 = Secao1.objects.all().first()
    secao2 = Secao2.objects.all()
    secao3 = Secao3.objects.all().first()
    secao4 = Secao4.objects.all().first()
    secao5 = Secao5.objects.all().first()
   
    form_cliente = FormClientes()
    form = FormEmailContato()
    form_email_novidades = FormNewslatter()
    
    context = {
                'form_cliente': form_cliente,
                'form': form,
                'form_email_novidades':form_email_novidades,
        
                ## SECOES
                'secao1': secao1,
                'secao2': secao2,
                'secao4': secao4,
                'secao3': secao3,
                'secao5': secao5,
           

                
                }

    if request.method == 'GET':
        return render(request, 'index.html', context )
    elif request.method == 'POST':
        return render(request, 'index.html', context)
    