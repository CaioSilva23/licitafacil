# Generated by Django 4.1.4 on 2023-03-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0020_remove_secao2_cards_secao2_cards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secao2',
            name='cards',
        ),
        migrations.AddField(
            model_name='secao2',
            name='cards',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plataforma.card'),
        ),
    ]