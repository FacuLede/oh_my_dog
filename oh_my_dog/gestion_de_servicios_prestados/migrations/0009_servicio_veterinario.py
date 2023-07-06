# Generated by Django 3.2.16 on 2023-07-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios_prestados', '0008_auto_20230622_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio_veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'servicio_veterinario',
                'verbose_name_plural': 'servicios_veterinarios',
            },
        ),
    ]
