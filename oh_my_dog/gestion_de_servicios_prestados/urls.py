from django.urls import path
from gestion_de_servicios_prestados import views

urlpatterns = [
    path('paseadores',views.paseadores, name= "paseadores"),    
    path('cuidadores',views.cuidadores, name= "cuidadores"),    
    path('contacto/<id>/',views.contacto, name= "contacto"),    #/<id>/
    path('contacto_cuidador/<id>/',views.contacto_cuidador, name= "contacto_cuidador"), 
]
