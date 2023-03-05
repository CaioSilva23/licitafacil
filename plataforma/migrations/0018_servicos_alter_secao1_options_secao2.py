# Generated by Django 4.1.4 on 2023-03-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0017_secao1_remove_plataforma_botao1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='secao1',
            options={'verbose_name_plural': 'Seção 1 - Home'},
        ),
        migrations.CreateModel(
            name='Secao2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('servicos', models.ManyToManyField(related_name='card_servicos', to='plataforma.servicos')),
            ],
            options={
                'verbose_name_plural': 'Secao 2 - Serviços',
            },
        ),
    ]