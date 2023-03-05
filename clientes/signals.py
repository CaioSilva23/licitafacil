from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente, EmailContato
from clientes.send_email import EnviaEmailCadastro, EnviaEmailContato

@receiver(post_save, sender=Cliente)
def send_mail_licitafacil(sender, instance, created, **kwargs):
    print('teste')
    if created:
        print('teste2')
        send_mail = EnviaEmailCadastro(instance)
        send_mail.cadastro_email()
 

@receiver(post_save, sender=EmailContato)
def send_mail_licitafacil(sender, instance, created, **kwargs):
    if created:
        send_mail = EnviaEmailContato(instance)
        send_mail.mail_contato()
 