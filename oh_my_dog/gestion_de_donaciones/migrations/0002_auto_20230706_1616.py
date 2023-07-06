# Generated by Django 3.2.16 on 2023-07-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_donaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campania_de_donacion',
            name='activa',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='campania_de_donacion',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='campania_de_donacion',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
    ]
