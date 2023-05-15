from django import forms 
from .models import Perro_perdido, Perro_en_adopcion

class  Perro_perdido_form(forms.ModelForm):
    # creted_by = forms.CharField(max_length=8)
    class Meta:
        model = Perro_perdido
        fields = [
            "nombre",
            "imagen",
            "descripcion",
            "telefono",
        ]
    # def __init__(self, *args, **kwargs):
    #     self.creted_by = kwargs.pop('dni', None)
    #     super(Perro_perdido_form, self).__init__(*args, **kwargs)
        # dni = kwargs.pop('request', None) # obtener el request de los argumentos
        # super(Perro_perdido_form, self).__init__(*args, **kwargs)
        # self.fields['created_by'].initial = dni # establecer el valor inicial del campo usuario
        # self.created_by = forms.CharField(max_length=8, initial=request.user.dni)

class Perro_en_adopcion_form(forms.ModelForm) :
    class Meta:
        model = Perro_en_adopcion
        fields = [
            "edad",
            "descripcion",
            "localidad",
        ]

