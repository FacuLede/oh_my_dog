# Generated by Django 3.2.16 on 2023-05-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0010_auto_20230521_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='detalles_de_salud',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='edad',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='historia',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='tamanio',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='titulo',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='perro_en_adopcion',
            name='zona',
            field=models.CharField(default='None', max_length=100),
        ),
    ]