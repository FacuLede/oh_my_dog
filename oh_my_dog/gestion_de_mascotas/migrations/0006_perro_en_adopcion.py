# Generated by Django 3.2.16 on 2023-04-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0005_perro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perro_en_adopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('localidad', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'perro_en_adopcion',
                'verbose_name_plural': 'perros_en_adopcion',
            },
        ),
    ]
