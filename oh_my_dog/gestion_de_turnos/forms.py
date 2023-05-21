from django import forms 
from .models import Turno
from datetime import date

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
            'fecha': forms.DateInput(attrs={'type': 'date','min': date.today().strftime('%Y-%m-%d')})
        }
        exclude = ['estado','dni_creator']

        