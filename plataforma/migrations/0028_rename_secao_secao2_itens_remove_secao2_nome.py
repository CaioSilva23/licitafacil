# Generated by Django 4.1.4 on 2023-03-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0027_alter_servicos_options_secao2_descricao_secao2_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secao2',
            old_name='secao',
            new_name='itens',
        ),
        migrations.RemoveField(
            model_name='secao2',
            name='nome',
        ),
    ]