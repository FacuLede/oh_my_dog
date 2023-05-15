from django.urls import path
from gestion_de_turnos import views

urlpatterns = [
    path('sacar_turno',views.sacar_turno, name= "sacar_turno"),
]