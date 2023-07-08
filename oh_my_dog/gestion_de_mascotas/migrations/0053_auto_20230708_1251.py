# Generated by Django 3.2.16 on 2023-07-08 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_mascotas', '0052_auto_20230708_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libreta_sanitaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('castrado', models.BooleanField(default=False)),
                ('ultima_desparasitacion', models.DateField(null=True)),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_mascotas.perro')),
            ],
            options={
                'verbose_name': 'libreta_sanitaria',
                'verbose_name_plural': 'libretas_sanitarias',
            },
        ),
        migrations.DeleteModel(
            name='Libreta_salitaria',
        ),
    ]
