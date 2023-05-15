from django.contrib import admin
from .models import Perro_perdido, Perro_encontrado, Perro, Perro_en_adopcion

# Register your models here.

class Perro_perdido_admin(admin.ModelAdmin):
    readonly_fields=('created','updated') 
class Perro_encontrado_admin(admin.ModelAdmin):
    readonly_fields=('created','updated') 
class Perro_admin(admin.ModelAdmin):
    pass
class Perro_en_adopcion_admin(admin.ModelAdmin):
    readonly_fields=('created','updated') 


admin.site.register(Perro_perdido, Perro_perdido_admin)
admin.site.register(Perro_encontrado, Perro_encontrado_admin)
admin.site.register(Perro, Perro_admin)
admin.site.register(Perro_en_adopcion, Perro_en_adopcion_admin)
