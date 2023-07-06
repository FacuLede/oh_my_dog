from django.db import models

# Create your models here.

class Campania_de_donacion(models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=50)
    descripcion = models.CharField(verbose_name="Descripción",max_length=200)
    monto_esperado = models.FloatField()
    activa = models.BooleanField(default=True)

    class Meta:
        unique_together = (('titulo','monto_esperado'))
        verbose_name='campaña_de_donacion'
        verbose_name_plural='campañas_de_donaciones'

    def __str__ (self):
        return self.titulo