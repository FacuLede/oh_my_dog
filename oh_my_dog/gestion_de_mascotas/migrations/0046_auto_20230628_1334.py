# Generated by Django 3.2.16 on 2023-06-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0045_rename_raza_raza_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='raza',
        ),
        migrations.AddField(
            model_name='perro',
            name='raza',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.raza'),
            preserve_default=False,
        ),
    ]
