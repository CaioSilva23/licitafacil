from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente
from clientes.send_email import EnviaEmail

@receiver(post_save, sender=Cliente)
def send_mail_licitafacil(sender, instance, created, **kwargs):
    if created:
        send_mail = EnviaEmail(instance)
        send_mail.cadastro_email()
 