# Generated by Django 4.1.4 on 2023-03-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0016_delete_email_delete_emailcontato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secao1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botao1', models.CharField(max_length=25, verbose_name='Botão 1')),
                ('botao2', models.CharField(max_length=25, verbose_name='Botão 2')),
                ('botao3', models.CharField(max_length=25, verbose_name='Botão 3')),
                ('botao4', models.CharField(max_length=25, verbose_name='Botão 4')),
                ('botao5', models.CharField(max_length=25, verbose_name='Botão 5')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='Logo da empresa')),
                ('logo_titulo', models.CharField(max_length=25, verbose_name='Nome da empresa')),
                ('titulo_inicial', models.CharField(max_length=100)),
                ('paragrafo_inicial', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='botao1',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='botao2',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='botao3',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='botao4',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='botao5',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='logo_img',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='logo_title',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='paragrafo_inicial',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='titulo_inicial',
        ),
    ]
