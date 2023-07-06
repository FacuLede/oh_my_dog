from django.db import models
from user.models import User
from gestion_de_servicios_prestados.models import Servicio_veterinario
from gestion_de_mascotas.models import Perro
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
    motivo = models.ForeignKey(Servicio_veterinario, on_delete=models.CASCADE, default=None, null=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, default="Pendiente", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, blank=True, default=None, null=True)
    class Meta:
        # unique_together = (('franja_horaria','fecha'))
        verbose_name='turno'
        verbose_name_plural='turnos'
    def __str__ (self):
        return self.motivo


