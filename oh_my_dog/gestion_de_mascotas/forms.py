from django import forms 
from .models import Perro_perdido, Perro_en_adopcion, Perro, Perro_encontrado, Raza, Entrada
from datetime import date
from gestion_de_servicios_prestados.models import Servicio_veterinario

class  Perro_perdido_form(forms.ModelForm):
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label='Ninguno')
    opciones_sexo = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    opciones_edad = [
        ('Cachorro', 'Cachorro'),
        ('Adulto', 'Adulto'),
        ('Anciano', 'Anciano'),
    ]
    edad = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_edad, label="Etapa de vida")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    opciones_franja_horaria = [
        ('Mañana', 'Mañana'),
        ('Medio día', 'Medio día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Madrugada', 'Madrugada'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_franja_horaria, label="Se me perdió en:")
    descripcion =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Perro_perdido
        fields = [
            "nombre",            
            "size",
            "sexo",
            "raza",
            "edad",
            "franja_horaria",
            "zona",            
            "descripcion",     
            "imagen",       
            "fecha_perdido",
        ]
        widgets = {
            'fecha_perdido': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        }

class  Perro_encontrado_form(forms.ModelForm):
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label='Ninguno')
    opciones_franja_horaria = [
        ('Mañana', 'Mañana'),
        ('Medio día', 'Medio día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Madrugada', 'Madrugada'),
    ]    
    opciones_sexo = [
        ('Macho ', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    opciones_edad = [
        ('Cachorro', 'Cachorro'),
        ('Adulto', 'Adulto'),
        ('Anciano', 'Anciano'),
    ]
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_franja_horaria, label="Lo encontré en:")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    edad = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_edad, label="Etapa de vida")    
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    descripcion =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Perro_encontrado
        fields = [
            "titulo",            
            "edad",
            "size",
            "sexo",
            "raza",            
            "imagen",
            "descripcion",
            "franja_horaria",            
            "zona",            
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
    opciones_sexo = [
        ('Macho ', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    titulo = forms.CharField(label="Título")
    historia = forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Perro_en_adopcion
        fields = [
            "titulo",
            "edad",
            "tamanio",
            "sexo",
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
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label='Ninguno')
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    opciones_sexo = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    class Meta:
        model = Perro
        fields = [
            "nombre",
            "size",
            "raza",
            "sexo",
            "nacimiento",
        ]
        widgets = {
            'nacimiento': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        }

class  Perro_perdido_update_form(forms.ModelForm):
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    nueva_imagen = forms.ImageField(required=False)
    opciones_franja_horaria = [
        ('Mañana', 'Mañana'),
        ('Medio día', 'Medio día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Madrugada', 'Madrugada'),
    ]    
    opciones_sexo = [
        ('Macho ', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    opciones_edad = [
        ('Cachorro', 'Cachorro'),
        ('Adulto', 'Adulto'),
        ('Anciano', 'Anciano'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_franja_horaria, label="Se me perdió en:")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    edad = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_edad, label="Etapa de")
    descripcion =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    fecha_perdido = forms.DateField(label='Se perdió el')

    def clean_fecha_perdido(self):
        fecha_ingresada = self.cleaned_data['fecha_perdido']
        fecha_actual = date.today()
        
        if fecha_ingresada > fecha_actual:
            raise forms.ValidationError("No puede ser una fecha futura.")
        
        return fecha_ingresada

    class Meta:
        model = Perro_perdido
        fields = [
            "nombre",
            "edad",
            "size",
            "fecha_perdido",
            "franja_horaria",
            "sexo",
            "raza",
            "zona",            
            "descripcion",  
            'nueva_imagen',            
        ]

class  Perro_encontrado_update_form(forms.ModelForm):
    opciones_franja_horaria = [
        ('Mañana', 'Mañana'),
        ('Medio día', 'Medio día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Madrugada', 'Madrugada'),
    ]    
    opciones_sexo = [
        ('Macho ', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    opciones_edad = [
        ('Cachorro', 'Cachorro'),
        ('Adulto', 'Adulto'),
        ('Anciano', 'Anciano'),
    ]
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_franja_horaria, label="Lo encontré en:")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    edad = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_edad, label="Etapa de")  
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    descripcion =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    nueva_imagen = forms.ImageField(required=False)
    fecha_encontrado = forms.DateField(label='Se encontró el')
    def clean_fecha_encontrado(self):
        fecha_ingresada = self.cleaned_data['fecha_encontrado']
        fecha_actual = date.today()
        
        if fecha_ingresada > fecha_actual:
            raise forms.ValidationError("No puede ser una fecha futura.")
        
        return fecha_ingresada
    class Meta:
        model = Perro_encontrado
        fields = [
            "titulo",
            "edad",
            "size",
            "sexo",            
            "raza",
            'nueva_imagen',
            "descripcion",
            "fecha_encontrado",
            "franja_horaria",
            "zona",           
        ]
        # widgets = {
        #     'fecha_encontrado': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')})
        # }

class Perro_form_update(forms.ModelForm) :
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label='Ninguno')
    opciones_size = [
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    opciones_sexo = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    size = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_size, label="Tamaño")
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=opciones_sexo, label="Sexo")
    class Meta:
        model = Perro
        fields = [
            "nombre",
            "size",
            "raza",
            "sexo",
        ]
       
class Entrada_form(forms.ModelForm):
    # motivo =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    motivo = forms.ModelChoiceField(queryset=Servicio_veterinario.objects.all(), empty_label='Selecciona un motivo')
    descripcion =  forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":"5"}))
    seguimiento =  forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model = Entrada
        fields = [
            "peso",
            "motivo",
            "descripcion",
            "seguimiento",            
        ]