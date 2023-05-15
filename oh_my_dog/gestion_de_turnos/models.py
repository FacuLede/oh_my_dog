from django.db import models

# Create your models here.


class Franja_horaria(models.Model) :
    franja = models.CharField(max_length=50)

    class Meta:
        verbose_name='franja_horaria'
        verbose_name_plural='franjas_horarias'
    def __str__ (self):
        return self.franja

class Turno(models.Model) :
    # franja_horaria = models.ManyToManyField(Franja_horaria)
    franja_horaria = models.CharField(max_length=50)
    motivo = models.TextField(max_length=100)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, default="Pendiente", blank=True)

    class Meta:
        unique_together = (('franja_horaria','fecha'))
        verbose_name='turno'
        verbose_name_plural='turnos'
    def __str__ (self):
        return self.motivo


