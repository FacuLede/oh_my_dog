from django.urls import path
from gestion_de_mascotas import views

urlpatterns = [
    path('perros_perdidos',views.perros_perdidos, name= "perros_perdidos"),
    path('anunciar_perro_perdido',views.anunciar_perro_perdido, name= "anunciar_perro_perdido"),
    path('anunciar_perro_adopcion',views.anunciar_perro_adopcion, name= "anunciar_perro_adopcion"),
    path('perros_en_adopcion',views.perros_en_adopcion, name= "perros_en_adopcion"),
    path('mis_perros',views.mis_perros, name= "mis_perros"),
]
