from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente, EmailContato
from clientes.tasks import cadastro_email, mail_contato


@receiver(post_save, sender=Cliente)
def send_mail_licitafacil_cadastro(sender, instance, created, **kwargs):
    if created:
        id = instance.id
        cadastro_email.delay(id)
 

@receiver(post_save, sender=EmailContato)
def send_mail_licitafacil_contato(sender, instance, created, **kwargs):
    if created:
        id = instance.id
        mail_contato.delay(id)
