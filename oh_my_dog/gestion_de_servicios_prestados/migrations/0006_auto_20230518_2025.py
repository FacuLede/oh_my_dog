# Generated by Django 3.2.16 on 2023-05-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios_prestados', '0005_auto_20230518_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidador',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paseador',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
