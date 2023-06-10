# Generated by Django 3.2.16 on 2023-06-09 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0028_auto_20230609_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='nacimiento',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perro',
            name='raza',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perro',
            name='sexo',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]