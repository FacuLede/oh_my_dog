from django.urls import path
from gestion_de_clientes import views

urlpatterns = [
    path('clientes',views.clientes, name= "clientes"),    
]