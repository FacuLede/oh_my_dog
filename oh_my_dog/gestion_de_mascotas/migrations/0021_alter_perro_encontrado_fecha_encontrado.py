# Generated by Django 3.2.16 on 2023-05-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0020_auto_20230526_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro_encontrado',
            name='fecha_encontrado',
            field=models.DateField(),
        ),
    ]
