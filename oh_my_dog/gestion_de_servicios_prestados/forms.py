from django import forms
from django.db import models
from .models import Paseador, Cuidador

class Send_email_form(forms.Form):
    mensaje =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))
    email = forms.EmailField(max_length=100, required=True )

class Send_email_logged_form(forms.Form):
    mensaje =  forms.CharField(max_length=100,widget=forms.Textarea(attrs={"rows":"5"}))


class Paseador_form(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=300,widget=forms.Textarea(attrs={"rows":"5"}))
    email = forms.EmailField(max_length=50)
    class Meta:
        model = Paseador
        fields = [
            "nombre",
            "descripcion",
            "email",
        ]

class Cuidador_form(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=300,widget=forms.Textarea(attrs={"rows":"5"}))
    email = forms.EmailField(max_length=50)
    class Meta:
        model = Cuidador
        fields = [
            "nombre",
            "descripcion",
            "email",
        ]