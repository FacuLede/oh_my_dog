# Generated by Django 3.2.16 on 2023-04-28 03:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios_prestados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuidador',
            name='email',
            field=models.EmailField(default=datetime.datetime(2023, 4, 28, 3, 12, 39, 60824, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paseador',
            name='email',
            field=models.EmailField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
