from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from emails.send_email import EnviaEmail
from emails.models import EmailContato


@receiver(post_save, sender=EmailContato)
def send_mail_licitafacil(sender, instance, created, **kwargs):
    if created:
        send_mail = EnviaEmail(instance)
        send_mail.mail_contato()
 