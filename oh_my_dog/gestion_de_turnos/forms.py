from django import forms 
from .models import Turno
from datetime import date, timedelta

class  Turno_form(forms.ModelForm):

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

        