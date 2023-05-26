from django import forms 
from .models import Perro_perdido, Perro_en_adopcion, Perro, Perro_encontrado
from datetime import date

class  Perro_perdido_form(forms.ModelForm):
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    class Meta:
        model = Perro_perdido
        fields = [
            "nombre",
            "edad",
            "size",
            "zona",            
            "descripcion",     
            "imagen",       
            "fecha_perdido",
        ]
        widgets = {
            'fecha_perdido': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        }

class  Perro_encontrado_form(forms.ModelForm):
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    class Meta:
        model = Perro_encontrado
        fields = [
            "zona",
            "imagen",
            "descripcion",
            "size",
            "fecha_encontrado",
        ]
        widgets = {
            'fecha_encontrado': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        }

class Perro_en_adopcion_form(forms.ModelForm) :
    opciones_edad = [
        ('Cachorro', 'Cachorro'),
        ('Adulto', 'Adulto'),
        ('Anciano', 'Anciano'),
    ]
    edad = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_edad)
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    tamanio = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    titulo = forms.CharField(label="Título")
    historia = forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Perro_en_adopcion
        fields = [
            "titulo",
            "edad",
            "tamanio",
            "detalles_de_salud",
            "zona",
            "historia",
        ]

class Send_email_form(forms.Form):
    mensaje =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    email = forms.EmailField(max_length=100, required=True )

class Send_email_logged_form(forms.Form):
    mensaje =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))

class Perro_form(forms.ModelForm) :

    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    class Meta:
        model = Perro
        fields = [
            "nombre",
            "edad",
            "peso",
            "size",
            "dni_owner",
        ]

class  Perro_perdido_update_form(forms.ModelForm):
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    nueva_imagen = forms.ImageField(required=False)
    class Meta:
        model = Perro_perdido
        fields = [
            "nombre",
            "edad",
            "size",
            "zona",            
            "descripcion",  
            'nueva_imagen',
        ]

class  Perro_encontrado_update_form(forms.ModelForm):
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    nueva_imagen = forms.ImageField(required=False)
    class Meta:
        model = Perro_encontrado
        fields = [
            "zona",
            "descripcion",
            "size",
            'nueva_imagen',
        ]
        # widgets = {
        #     'fecha_encontrado': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        # }

