from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente, EmailContato
#from clientes.send_email import EnviaEmailContato
from clientes.tasks import cadastro_email


@receiver(post_save, sender=Cliente)
def send_mail_licitafacil_cadastro(sender, instance, created, **kwargs):
    if created:
        id = instance.id
        cadastro_email.delay(id)
 

# @receiver(post_save, sender=EmailContato)
# def send_mail_licitafacil_contato(sender, instance, created, **kwargs):
#     if created:
#         send_mail = EnviaEmailContato(instance)
#         send_mail.mail_contato()
 
