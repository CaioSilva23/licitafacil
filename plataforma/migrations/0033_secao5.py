# Generated by Django 4.1.4 on 2023-03-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0032_delete_plataforma_alter_secao3_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secao5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('paragrafo', models.TextField(max_length=3000)),
            ],
            options={
                'verbose_name_plural': 'Seção 5 - Sobre a empresa',
            },
        ),
    ]