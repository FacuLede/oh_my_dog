from django import forms 
from .models import Turno

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
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ['estado']

        