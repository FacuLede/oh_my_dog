# Generated by Django 3.2.16 on 2023-06-09 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0034_auto_20230609_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro_perdido',
            name='raza',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]