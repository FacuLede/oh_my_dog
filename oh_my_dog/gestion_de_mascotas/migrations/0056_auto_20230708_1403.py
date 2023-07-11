# Generated by Django 3.2.16 on 2023-07-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0055_auto_20230708_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='numero_dosis',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='vacuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.vacuna'),
        ),
    ]