# Generated by Django 3.2.16 on 2023-07-11 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0063_perro_perdido_nueva_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro_perdido',
            name='nueva_imagen',
        ),
    ]
