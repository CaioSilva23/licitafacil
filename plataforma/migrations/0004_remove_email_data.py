# Generated by Django 4.1.4 on 2022-12-29 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_remove_emailcontato_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='data',
        ),
    ]
