from django.db import models
from user.models import User
from gestion_de_servicios_prestados.models import Servicio_veterinario
from django.core.validators import MinValueValidator
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

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:        
        verbose_name='vacuna'
        verbose_name_plural='vacunas'

    def __str__ (self):
        return self.nombre

class Entrada(models.Model):
    fecha = models.DateField(auto_now_add=True)
    peso = models.FloatField(validators=[MinValueValidator(0)])
    motivo = models.ForeignKey(Servicio_veterinario, on_delete=models.CASCADE, null=True, blank=True, default=None)
    # motivo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    seguimiento = models.CharField(max_length=500)
    numero_dosis = models.PositiveBigIntegerField(null=True, blank=True)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE, null=True, blank=True) 
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    class Meta:        
        verbose_name='entrada'
        verbose_name_plural='entradas'

    def __str__ (self):
        return self.motivo

class Libreta_sanitaria(models.Model):
    castrado = models.BooleanField(default=False)
    ultima_desparasitacion = models.DateField(null=True)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    class Meta:        
        verbose_name='libreta_sanitaria'
        verbose_name_plural='libretas_sanitarias'

    def __str__ (self):
        return self.perro

class Registro_vacuna(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    numero_dosis = models.PositiveIntegerField()

    class Meta:        
        verbose_name='registro_vacuna'
        verbose_name_plural='registros_vacunas'

    def __str__ (self):
        return self.vacuna