# Generated by Django 3.2.16 on 2023-07-08 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0053_auto_20230708_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='numero_dosis',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='vacuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.vacuna'),
        ),
    ]
