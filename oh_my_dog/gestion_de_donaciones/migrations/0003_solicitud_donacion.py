# Generated by Django 3.2.16 on 2023-07-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_donaciones', '0002_auto_20230706_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud_donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
