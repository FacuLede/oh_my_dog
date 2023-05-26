from django.urls import path
from gestion_de_servicios_prestados import views

urlpatterns = [
    path('paseadores',views.paseadores, name= "paseadores"),    
    path('cuidadores',views.cuidadores, name= "cuidadores"),    
    path('contacto/<id>/',views.contacto, name= "contacto"),   
    path('contacto_cuidador/<id>/',views.contacto_cuidador, name= "contacto_cuidador"), 
    path('cargar_paseador',views.cargar_paseador, name= "cargar_paseador"), 
    path('cargar_cuidador',views.cargar_cuidador, name= "cargar_cuidador"),
    path('editar_paseador/<id>/',views.editar_paseador, name= "editar_paseador"), 
    path('editar_cuidador/<id>/',views.editar_cuidador, name= "editar_cuidador"),     
    path('eliminar_paseador/<id>/',views.eliminar_paseador, name= "eliminar_paseador"), 
    path('eliminar_cuidador/<id>/',views.eliminar_cuidador, name= "eliminar_cuidador"), 
]
