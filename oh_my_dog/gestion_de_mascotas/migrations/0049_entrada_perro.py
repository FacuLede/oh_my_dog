# Generated by Django 3.2.16 on 2023-07-01 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0048_entrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='perro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.perro'),
            preserve_default=False,
        ),
    ]