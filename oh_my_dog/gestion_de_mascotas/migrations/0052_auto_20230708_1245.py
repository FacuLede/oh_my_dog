# Generated by Django 3.2.16 on 2023-07-08 15:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0051_alter_entrada_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='peso',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dosis', models.PositiveIntegerField()),
                ('fecha', models.DateField()),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.perro')),
            ],
            options={
                'verbose_name': 'vacuna',
                'verbose_name_plural': 'vacunas',
            },
        ),
        migrations.CreateModel(
            name='Libreta_salitaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('castrado', models.BooleanField(default=False)),
                ('ultima_desparasitacion', models.DateField()),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.perro')),
            ],
            options={
                'verbose_name': 'libreta_sanitaria',
                'verbose_name_plural': 'libretas_sanitarias',
            },
        ),
    ]
