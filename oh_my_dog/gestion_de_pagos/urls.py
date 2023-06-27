from django.urls import path
from gestion_de_pagos import views

urlpatterns = [
    path('formulario_de_pago',views.formulario_de_pago, name= "formulario_de_pago"),    
]