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

    banner = models.ImageField(blank=True, upload_to='banner')

    def __str__(self) -> str:
        return f'Seção 1 - Home'

    class Meta:
        verbose_name_plural = 'Seção 1 - Home'


class Servicos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Add seus serviços'


class Secao2(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    saiba_mais = models.TextField(max_length=3000)
    link = models.URLField(max_length=200, null=True, blank=True)
    itens = models.ManyToManyField(Servicos, related_name='secao_servicos')
    preco = models.FloatField()


    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name_plural = 'Secao 2 - Serviços'



class Secao3(models.Model):
    titulo = models.CharField(max_length=100)
    paragrafo = models.TextField(max_length=3000)

    def __str__(self) -> str:
        return 'Seção - Nosso diferencial'

    class Meta:
        verbose_name_plural = 'Seção 3 - Nosso diferencial'

class Secao4(models.Model):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return 'Seção de contato'

    class Meta:
        verbose_name_plural = 'Seção 4 - Contatos'



class Secao5(models.Model):
    titulo = models.CharField(max_length=100)
    paragrafo = models.TextField(max_length=3000)

    def __str__(self) -> str:
        return 'Seção - Sobre a empresa'

    class Meta:
        verbose_name_plural = 'Seção 5 - Sobre a empresa'