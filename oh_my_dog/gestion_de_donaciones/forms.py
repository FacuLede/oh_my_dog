from django import forms 
from .models import Campania_de_donacion, Solicitud_donacion

class  Campania_form(forms.ModelForm):
    descripcion =  forms.CharField(max_length=200,widget=forms.Textarea(attrs={"rows":"5"}))
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