# Generated by Django 4.1.4 on 2023-01-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_plataforma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='paragrafo',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='titulo',
            field=models.TextField(max_length=200),
        ),
    ]
