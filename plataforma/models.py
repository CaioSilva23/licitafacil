from django.db import models
from django.utils.timezone import now


class Secao1(models.Model):
    # LINKS
    botao1 = models.CharField(max_length=25, verbose_name='Botão 1')
    botao2 = models.CharField(max_length=25, verbose_name='Botão 2')
    botao3 = models.CharField(max_length=25, verbose_name='Botão 3')
    botao4 = models.CharField(max_length=25, verbose_name='Botão 4')
    botao5 = models.CharField(max_length=25, verbose_name='Botão 5')

    # LOGO
    logo = models.ImageField(upload_to='logo', verbose_name='Logo da empresa')
    logo_titulo = models.CharField(max_length=25, verbose_name='Nome da empresa')

    # INICIAL
    titulo_inicial = models.CharField(max_length=100)
    paragrafo_inicial = models.TextField(max_length=200)

    def __str__(self) -> str:
        return f'Seção 1 - Home'

    class Meta:
        verbose_name_plural = 'Seção 1 - Home'


class Secao2(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'Secao 2 - Serviços'

    class Meta:
        verbose_name_plural = 'Secao 2 - Serviços'


class Servicos(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Serviços'

class Card(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    servicos = models.ManyToManyField(Servicos, related_name='card_servicos')
    secao = models.ForeignKey(Secao2, on_delete=models.SET_NULL, null=True)



class Secao4(models.Model):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return 'Seção de contato'

    class Meta:
        verbose_name_plural = 'Seção 4 - Contatos'


# class Secao4(models.Model):
#     pass

# class Secao5(models.Model):
#     pass

# class Secao6(models.Model):
#     pass




class Plataforma(models.Model):
 
    # SERVICOS
    preco_servico1 = models.IntegerField()
    preco_servico2 = models.IntegerField()


    # SICAF
    sicaf_titulo = models.CharField(max_length=50)
    sicaf_texto = models.TextField()

    # sobre licita facil

    licitafacil_titulo = models.CharField(max_length=100)
    licitafacil_texto = models.TextField()





    def __str__(self) -> str:
        return f'Informações da plataforma'