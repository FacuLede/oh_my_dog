from django.contrib import admin
from .models import User
# Register your models here.

class Usuario_admin(admin.ModelAdmin):
    pass

admin.site.register(User, Usuario_admin)