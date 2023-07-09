# Generated by Django 3.2.16 on 2023-07-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios_prestados', '0009_servicio_veterinario'),
        ('gestion_de_mascotas', '0057_registro_vacuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='motivo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_servicios_prestados.servicio_veterinario'),
        ),
    ]
