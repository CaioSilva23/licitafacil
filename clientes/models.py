from django.db import models
from plataforma.models import Secao2

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=15)
    servico = models.ForeignKey(Secao2, on_delete=models.SET_NULL, null=True)
   
    class Meta:
        verbose_name_plural = 'Clientes cadastrados'

    def __str__(self) -> str:
        return f'Cliente: {self.nome}'


# BACK-END
class Newslatter(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name_plural = 'Inscrições newslatter'

class EmailContato(models.Model):
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self) -> str:
        return f'{self.email} - {self.assunto}'

    class Meta:
        verbose_name_plural = 'Formulários de contato'







        