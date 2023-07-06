from django import forms 
from .models import Campania_de_donacion

class  Campania_form(forms.ModelForm):
    descripcion =  forms.CharField(max_length=200,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Campania_de_donacion
        fields = [
            "titulo",            
            "descripcion",
            "monto_esperado",
        ]