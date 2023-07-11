from django import forms 
from .models import Campania_de_donacion, Solicitud_donacion
from django.core.exceptions import ValidationError

class  Campania_form(forms.ModelForm):
    descripcion =  forms.CharField(max_length=200,widget=forms.Textarea(attrs={"rows":"5"}))
    def clean_monto_esperado(self):
        monto = self.cleaned_data['monto_esperado']
        if float(monto) <= 0 :            
            raise ValidationError('Ingrese un monto válido')
        return monto
    class Meta:
        model = Campania_de_donacion
        fields = [
            "titulo",            
            "descripcion",
            "monto_esperado",
        ]

class Donar_form(forms.ModelForm) :
    nombre  = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    class Meta:
        model = Solicitud_donacion
        fields = [
            "nombre",            
            "apellido",
            "email",
        ]