from django.urls import path
from gestion_de_usuarios import views
from gestion_de_usuarios.views import Registrarse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name= "home"),
    path('iniciar_sesion',views.iniciar_sesion, name= "iniciar_sesion"),
    path('registrarse',Registrarse.as_view(), name= "registrarse"),
    path('cerrar_sesion',views.cerrar_sesion, name= "cerrar_sesion"),
    path('perfil',views.perfil, name= "perfil"),
    path('editar_perfil',views.editar_perfil, name= "editar_perfil"),
    path('eliminar_usuario',views.eliminar_usuario, name= "eliminar_usuario"),
    path('change_password',views.change_password, name= "change_password"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
