from django.urls import path
from gestion_de_turnos import views

urlpatterns = [
    path('sacar_turno',views.sacar_turno, name= "sacar_turno"),
    path('turnos_pendientes',views.turnos_pendientes, name= "turnos_pendientes"),
    path('mis_turnos',views.mis_turnos, name= "mis_turnos"),
    path('eliminar_turno/<id>/<motivo>/',views.eliminar_turno, name= "eliminar_turno"),
    path('aprobar_turno/<id>/',views.aprobar_turno, name= "aprobar_turno"),
    path('rechazar_turno/<id>/',views.rechazar_turno, name= "rechazar_turno"),
    path('cancelar_turno/<id>/',views.cancelar_turno, name= "cancelar_turno"),
    path('turnos_aprobados',views.turnos_aprobados, name= "turnos_aprobados"),
    path('cancelar_turno_aprobado/<id>/<motivo>/',views.cancelar_turno_aprobado, name= "cancelar_turno_aprobado"),
]