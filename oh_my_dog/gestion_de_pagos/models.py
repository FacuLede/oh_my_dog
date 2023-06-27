from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Tarjeta(models.Model) :
    nombre_titular = models.CharField(max_length=50)
    apellido_titular = models.CharField(max_length=50)
    dni_titular = models.CharField(max_length=8)
    numero_tarjeta = models.CharField(max_length=16)
    mes_expiracion = models.PositiveIntegerField()
    anio_expiracion = models.PositiveIntegerField()
    cvv = models.CharField(max_length=4)
    class Meta:
        verbose_name='tarjeta'
        verbose_name_plural='tarjetas'
    def __str__ (self):
        return self.numero_tarjeta