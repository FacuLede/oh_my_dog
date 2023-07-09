from django.urls import path
from gestion_de_pagos import views

urlpatterns = [
    path('formulario_de_pago/<id>/<solicitud>/',views.formulario_de_pago, name= "formulario_de_pago"),    
    path('pagar/<id_campania>/<id_solicitud>/<id_tarjeta>/',views.pagar, name= "pagar"),    
]