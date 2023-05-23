from django.db import models
from user.models import User

# Create your models here.

class Perro_perdido(models.Model):
    """Estos registros los crea un usuario que perdió 
    a su perro"""
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='perros_perdidos')  
    descripcion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perro_perdido'
        verbose_name_plural='perros_perdidos'

    def __str__ (self):
        return self.nombre

class Perro_encontrado(models.Model):
    """Estos registros los crea un usuario que encontró
    un perro perdido"""
    imagen=models.ImageField(upload_to='perros_encontrados')
    descripcion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perro_encontrado'
        verbose_name_plural='perros_encontrados'

    def __str__ (self):
        return self.descripcion
    
class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    dni_owner = models.CharField(max_length=8)
    # owner = models.OneToOneField(User)

    class Meta:
        unique_together = (('nombre', 'dni_owner'))
        verbose_name='perro'
        verbose_name_plural='perros'

    def __str__ (self):
        return self.nombre
    
class Perro_en_adopcion(models.Model):
    titulo = models.CharField(max_length=30)    
    edad=models.CharField(max_length=30)
    tamanio = models.CharField(max_length=30)
    detalles_de_salud=models.CharField(max_length=200)
    zona=models.CharField(max_length=100)
    historia = models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perro_en_adopcion'
        verbose_name_plural='perros_en_adopcion'

    def __str__ (self):
        return self.titulo
    