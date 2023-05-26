from django.urls import path
from gestion_de_mascotas import views

urlpatterns = [
    path('perros_perdidos',views.perros_perdidos, name= "perros_perdidos"),
    path('perros_encontrados',views.perros_encontrados, name= "perros_encontrados"),
    path('anunciar_perro_perdido',views.anunciar_perro_perdido, name= "anunciar_perro_perdido"),
    path('anunciar_perro_adopcion',views.anunciar_perro_adopcion, name= "anunciar_perro_adopcion"),
    path('perros_en_adopcion',views.perros_en_adopcion, name= "perros_en_adopcion"),
    path('mis_perros',views.mis_perros, name= "mis_perros"),
    path('mis_perros_en_adopcion',views.mis_perros_en_adopcion, name= "mis_perros_en_adopcion"),
    path('eliminar_anuncio_adopcion/<id>/',views.eliminar_anuncio_adopcion, name= "eliminar_anuncio_adopcion"),
    path('contacto_adopcion/<id>/',views.contacto_adopcion, name= "contacto_adopcion"),
    path('editar_anuncio/<id>/',views.editar_anuncio, name= "editar_anuncio"),
    path('perros',views.perros, name= "perros"),
    path('cargar_perro',views.cargar_perro, name= "cargar_perro"),
    path('editar_perro/<id>/',views.editar_perro, name= "editar_perro"),
    path('eliminar_perro/<id>/',views.eliminar_perro, name= "eliminar_perro"),
    path('anunciar_perro_encontrado',views.anunciar_perro_encontrado, name= "anunciar_perro_encontrado"),
    path('eliminar_anuncio_encontrado/<id>/',views.eliminar_anuncio_encontrado, name= "eliminar_anuncio_encontrado"),
    path('eliminar_anuncio_perdido/<id>/',views.eliminar_anuncio_perdido, name= "eliminar_anuncio_perdido"),
    path('editar_anuncio_encontrado/<id>/',views.editar_anuncio_encontrado, name= "editar_anuncio_encontrado"),
    path('editar_anuncio_perdido/<id>/',views.editar_anuncio_perdido, name= "editar_anuncio_perdido"),
    path('contacto_encontrado/<id>/',views.contacto_encontrado, name= "contacto_encontrado"),
    path('contacto_perdido/<id>/',views.contacto_perdido, name= "contacto_perdido"),
    path('adopcion_realizada/<id>/',views.adopcion_realizada, name= "adopcion_realizada"),
]
