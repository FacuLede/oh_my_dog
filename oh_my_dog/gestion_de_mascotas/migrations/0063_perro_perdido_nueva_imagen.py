# Generated by Django 3.2.16 on 2023-07-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0062_libreta_sanitaria_anteultima_desparasitacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro_perdido',
            name='nueva_imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='perros_perdidos'),
        ),
    ]
