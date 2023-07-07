from django.db import models
from user.models import User
from gestion_de_servicios_prestados.models import Servicio_veterinario
# Create your models here.
class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta():
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

    def __str__(self) :
        return self.nombre

class Perro_perdido(models.Model):
    """Estos registros los crea un usuario que perdió 
    a su perro"""
    nombre=models.CharField(max_length=30)
    edad =  models.CharField(max_length=50) 
    size = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='perros_perdidos')      
    fecha_perdido = models.DateField()    
    zona = models.CharField(max_length=100)    
    franja_horaria = models.CharField(max_length=50)
    sexo = models.CharField(max_length=30)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, default=None, null=True)
    encontrado = models.BooleanField(default=False)
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
    titulo = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, default=None, null=True)
    franja_horaria = models.CharField(max_length=30)
    recuperado = models.BooleanField(default=False)
    #nuevos
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
    size = models.CharField(verbose_name="Tamaño", max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, default=None, null=True)
    # raza = models.CharField(max_length=50,null=True, default=None)
    sexo = models.CharField(max_length=30,null=True, default=None)
    nacimiento = models.DateField()
    # owner = models.OneToOneField(User)

    class Meta:
        unique_together = (('nombre', 'owner'))
        verbose_name='perro'
        verbose_name_plural='perros'

    def __str__ (self):
        return self.nombre
    
class Perro_en_adopcion(models.Model):
    titulo = models.CharField(max_length=30)    
    edad=models.CharField(max_length=30)
    tamanio = models.CharField(max_length=30)
    detalles_de_salud=models.CharField(max_length=200)
    sexo=models.CharField(max_length=30)
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
    
class Entrada(models.Model):
    fecha = models.DateField(auto_now_add=True)
    peso = models.FloatField()
    motivo = models.ForeignKey(Servicio_veterinario, on_delete=models.CASCADE)
    # motivo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    seguimiento = models.CharField(max_length=500)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    class Meta:        
        verbose_name='entrada'
        verbose_name_plural='entradas'

    def __str__ (self):
        return self.motivo
    