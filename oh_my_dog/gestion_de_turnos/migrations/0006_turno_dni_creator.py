# Generated by Django 3.2.16 on 2023-05-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_turnos', '0005_alter_turno_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='dni_creator',
            field=models.CharField(default=None, max_length=8, unique=True),
            preserve_default=False,
        ),
    ]
