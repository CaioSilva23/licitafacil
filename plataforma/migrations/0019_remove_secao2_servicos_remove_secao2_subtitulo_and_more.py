# Generated by Django 4.1.4 on 2023-03-02 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0018_servicos_alter_secao1_options_secao2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secao2',
            name='servicos',
        ),
        migrations.RemoveField(
            model_name='secao2',
            name='subtitulo',
        ),
        migrations.RemoveField(
            model_name='secao2',
            name='titulo',
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('servicos', models.ManyToManyField(related_name='card_servicos', to='plataforma.servicos')),
            ],
        ),
        migrations.AddField(
            model_name='secao2',
            name='cards',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plataforma.card'),
        ),
    ]