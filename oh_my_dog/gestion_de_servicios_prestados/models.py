from django.db import models

# Create your models here.

class Paseador(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    email = models.EmailField(max_length=50,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='paseador'
        verbose_name_plural='paseadores'
    def __str__ (self):
        return self.nombre
    
class Cuidador(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    email = models.EmailField(max_length=50,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='cuidador'
        verbose_name_plural='cuidadores'
    def __str__ (self):
        return self.nombre