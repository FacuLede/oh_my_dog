
from django import forms
from .models import Tarjeta
from datetime import date, timedelta
import datetime

class CreditCardForm(forms.ModelForm):
    nombre_titular = forms.CharField(label='Nombre del titular', max_length=100)
    apellido_titular = forms.CharField(label='Nombre del titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de tarjeta', max_length=16)    
    cvv = forms.CharField(label='CVV', max_length=4)
    nombre_titular = forms.CharField(label='Nombre del titular', max_length=100)
    apellido_titular = forms.CharField(label='Apellido del titular', max_length=100)    
    mes_expiracion = forms.IntegerField(label='Mes de expiración')
    anio_expiracion = forms.IntegerField(label='Año de expiración')    
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
       