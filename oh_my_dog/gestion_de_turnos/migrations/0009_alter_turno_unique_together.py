# Generated by Django 3.2.16 on 2023-05-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_turnos', '0008_auto_20230521_0753'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='turno',
            unique_together=set(),
        ),
    ]
