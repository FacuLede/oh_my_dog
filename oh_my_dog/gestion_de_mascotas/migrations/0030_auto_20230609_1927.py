# Generated by Django 3.2.16 on 2023-06-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0029_auto_20230609_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='raza',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perro',
            name='sexo',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]