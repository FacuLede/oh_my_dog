from django.contrib import admin
from .models import Paseador, Cuidador

# Register your models here.

class Paseador_admin(admin.ModelAdmin):
    readonly_fields=('created','updated') 
class Cuidador_admin(admin.ModelAdmin):
    readonly_fields=('created','updated') 


admin.site.register(Paseador, Paseador_admin)
admin.site.register(Cuidador, Cuidador_admin)