# Generated by Django 3.2.16 on 2023-05-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0015_auto_20230525_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='dni_owner',
            field=models.CharField(default=None, max_length=8, verbose_name='Dni del dueño'),
        ),
        migrations.AlterField(
            model_name='perro',
            name='edad',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='perro',
            name='peso',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='perro',
            name='size',
            field=models.CharField(default=None, max_length=50, verbose_name='Tamaño'),
        ),
    ]
