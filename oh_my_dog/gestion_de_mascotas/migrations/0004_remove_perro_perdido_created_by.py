# Generated by Django 3.2.16 on 2023-04-26 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0003_auto_20230425_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro_perdido',
            name='created_by',
        ),
    ]
