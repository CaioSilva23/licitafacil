# Generated by Django 4.1.4 on 2023-02-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_alter_plataforma_titulo_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcontato',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]