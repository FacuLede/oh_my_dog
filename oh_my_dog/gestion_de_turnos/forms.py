from django import forms 
from .models import Turno
from datetime import date, timedelta
from gestion_de_servicios_prestados.models import Servicio_veterinario
from gestion_de_mascotas.models import Perro

class  Turno_form(forms.ModelForm):
    motivo = forms.ModelChoiceField(queryset=Servicio_veterinario.objects.all(), empty_label='Elige un motivo')
    OPCIONES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=OPCIONES)
    def __init__(self, user, *args, **kwargs):
        super(Turno_form, self).__init__(*args, **kwargs)
        self.fields['perro'].queryset = Perro.objects.filter(owner=user)
        self.fields['perro'].empty_label = 'Ninguno'
    class Meta:
        model = Turno
        fields = [
            "franja_horaria",
            "motivo",
            "fecha",
            "perro"
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date','min': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')})
        }
        exclude = ['estado','dni_creator']    

class  Turno_form_perroless(forms.ModelForm):
    motivo = forms.ModelChoiceField(queryset=Servicio_veterinario.objects.all(), empty_label='Elige un motivo')
    OPCIONES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=OPCIONES)

    class Meta:
        model = Turno
        fields = [
            "franja_horaria",
            "motivo",
            "fecha",
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date','min': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')})
        }
        exclude = ['estado','dni_creator']    


class  Reprogramar_turno_form(forms.ModelForm):
    OPCIONES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    ]
    franja_horaria = forms.ChoiceField(widget=forms.RadioSelect, choices=OPCIONES)
    class Meta:
        model = Turno
        fields = [
            "franja_horaria",
            "fecha",
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date','min': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')})
        }
        exclude = ['motivo','estado','dni_creator']

        