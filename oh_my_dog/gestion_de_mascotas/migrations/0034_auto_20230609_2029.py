# Generated by Django 3.2.16 on 2023-06-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0033_auto_20230609_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro_perdido',
            name='franja_horaria',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perro_perdido',
            name='sexo',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
