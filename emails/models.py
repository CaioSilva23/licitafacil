from django.db import models


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


