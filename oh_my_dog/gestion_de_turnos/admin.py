from django.contrib import admin
from .models import Turno
# Register your models here.

class Turno_admin(admin.ModelAdmin):
    pass


admin.site.register(Turno, Turno_admin)