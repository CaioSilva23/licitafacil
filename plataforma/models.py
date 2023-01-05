from django.db import models
from django.utils.timezone import now

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