from django.urls import path
from gestion_de_turnos import views

urlpatterns = [
    path('sacar_turno',views.sacar_turno, name= "sacar_turno"),
    path('turnos_pendientes',views.turnos_pendientes, name= "turnos_pendientes"),
    path('mis_turnos',views.mis_turnos, name= "mis_turnos"),
    path('eliminar_turno/<id>/',views.eliminar_turno, name= "eliminar_turno"),
]