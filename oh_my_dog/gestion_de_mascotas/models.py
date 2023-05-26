from django.db import models
from user.models import User

# Create your models here.

class Perro_perdido(models.Model):
    """Estos registros los crea un usuario que perdió 
    a su perro"""
    nombre=models.CharField(max_length=30)
    edad =  models.IntegerField()
    size = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='perros_perdidos')      
    fecha_perdido = models.DateField()    
    zona = models.CharField(max_length=100)    
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
    un perro perdido quien debe tener perros a su nombre"""
    size = models.CharField(max_length=50)
    zona = models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='perros_encontrados')
    descripcion=models.CharField(max_length=100)
    fecha_encontrado = models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perro_encontrado'
        verbose_name_plural='perros_encontrados'

    def __str__ (self):
        return self.zona
    
class Perro(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=30)
    edad = models.CharField(verbose_name="Edad", max_length=100)
    peso = models.FloatField(verbose_name="Peso")
    size = models.CharField(verbose_name="Tamaño", max_length=50)
    dni_owner = models.CharField(max_length=8, verbose_name="Dni del dueño")
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
    adoptado = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perro_en_adopcion'
        verbose_name_plural='perros_en_adopcion'

    def __str__ (self):
        return self.titulo
    