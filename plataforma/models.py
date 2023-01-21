from django.db import models
from django.utils.timezone import now



# BACK-END
class Email(models.Model):
    email = models.EmailField()


    def __str__(self) -> str:
        return self.email

class EmailContato(models.Model):
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    texto = models.TextField()


    def __str__(self) -> str:
        return f'{self.email} - {self.assunto}'

class Plataforma(models.Model):
    # INICIAL
    titulo_inicial = models.CharField(max_length=100)
    paragrafo_inicial = models.TextField(max_length=200)

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