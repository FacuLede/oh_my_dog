from django.urls import path
from gestion_de_donaciones import views

urlpatterns = [
    path('crear_campania',views.crear_campania, name= "crear_campania"),
    path('ver_campanias_de_donacion',views.ver_campanias_de_donacion, name= "ver_campanias_de_donacion"),
    path('eliminar_campania/<id>/',views.eliminar_campania, name= "eliminar_campania"),
    path('editar_campania/<id>/',views.editar_campania, name= "editar_campania"),
    path('pausar_campania/<id>/',views.pausar_campania, name= "pausar_campania"),
    path('reanudar_campania/<id>/',views.reanudar_campania, name= "reanudar_campania"),
    path('donar/<id>/',views.donar, name= "donar"),
    path('ver_donaciones/<id>/',views.ver_donaciones, name= "ver_donaciones"),
]