# Generated by Django 3.2.16 on 2023-07-10 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0060_alter_entrada_numero_dosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_vacuna',
            name='entrada',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.entrada'),
            preserve_default=False,
        ),
    ]
