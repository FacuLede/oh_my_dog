# Generated by Django 3.2.16 on 2023-04-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0002_auto_20230425_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro_perdido',
            name='created_by',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='perro_perdido',
            name='imagen',
            field=models.ImageField(upload_to='perros_perdidos'),
        ),
    ]