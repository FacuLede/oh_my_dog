
from django import forms
from .models import Tarjeta
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError

class CreditCardForm(forms.ModelForm):
    nombre_titular = forms.CharField(label='Nombre del titular', max_length=100)
    apellido_titular = forms.CharField(label='Nombre del titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de tarjeta', max_length=16)    
    cvv = forms.CharField(label='CVV', max_length=4)
    nombre_titular = forms.CharField(label='Nombre del titular', max_length=100)
    apellido_titular = forms.CharField(label='Apellido del titular', max_length=100)    
    mes_expiracion = forms.IntegerField(label='Mes de expiración')
    anio_expiracion = forms.IntegerField(label='Año de expiración')    

    def clean_mes_expiracion(self):
        mes_expiracion = self.cleaned_data['mes_expiracion']
        if mes_expiracion < 1 or mes_expiracion > 12:
            raise ValidationError('Ingrese un mes válido')
        return mes_expiracion

    def clean_anio_expiracion(self):
        anio_expiracion = self.cleaned_data['anio_expiracion']
        if anio_expiracion < timezone.now().year:
            raise ValidationError('Ingrese un año válido')
        return anio_expiracion
    class Meta:
        model = Tarjeta
        fields = [            
            "nombre_titular",
            "apellido_titular",
            "dni_titular",
            "numero_tarjeta",            
            "cvv",
            "mes_expiracion",
            "anio_expiracion",
        ]
       
class Pagar(forms.Form):
    monto = forms.FloatField(label='Ingrese un monto')