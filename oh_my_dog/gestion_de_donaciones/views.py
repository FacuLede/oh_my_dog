from django.shortcuts import render, redirect, reverse
from .forms import Campania_form, Donar_form
from .models import Campania_de_donacion, Donacion
# Create your views here.

def crear_campania(request):
    form  = Campania_form()
    data = {
        "form":form,
    }
    if request.method == 'POST':
        form = Campania_form(request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = "Se ha creado la campaña exitosamente."
            return redirect(to="ver_campanias_de_donacion")
        else :
            data['error'] = "Esta campaña de donación ya existe."

    return render(request, "gestion_de_donaciones/crear_campania.html", data)

def ver_campanias_de_donacion(request):
    if request.user.is_superuser :
        campanias = Campania_de_donacion.objects.all()
    else :
        campanias = Campania_de_donacion.objects.filter(activa = True)
    return render(request, "gestion_de_donaciones/ver_campanias_de_donacion.html", {"campanias":campanias})

def eliminar_campania(request, id) :
    campania = Campania_de_donacion.objects.get(id = id)
    campania.delete()
    return redirect(to = request.META.get('HTTP_REFERER')) 

def editar_campania(request, id):    
    campania = Campania_de_donacion.objects.get(id = id) #obtiene la publicación que se quiere editar
    # current_user = request.user
    form = Campania_form(request.POST or None, instance = campania)
    data = {
        'form': form,
    } 
    if form.is_valid():
        campania.save()
        return redirect(to = "ver_campanias_de_donacion")
    else:
        return render(request,"gestion_de_donaciones/editar_campania.html",data)

def pausar_campania(request, id):
    campania = Campania_de_donacion.objects.get(id = id)
    campania.activa = False
    campania.save()
    return redirect(to = request.META.get('HTTP_REFERER')) 

def reanudar_campania(request, id):
    campania = Campania_de_donacion.objects.get(id = id)
    campania.activa = True
    campania.save()
    return redirect(to = request.META.get('HTTP_REFERER')) 

def donar(request, id) :
    data = {}
    if request.user.is_authenticated :
        form  = Donar_form(initial={'nombre': request.user.first_name,'apellido': request.user.last_name,'email': request.user.email, })
        data = {
            "form":form,
        }
    else:
        form  = Donar_form()
        data = {
            "form":form,
        }

    if request.method == 'POST' :
        form = Donar_form(request.POST) 
        if form.is_valid() :
            solicitud = form.save(commit = False)
            solicitud.save()
            params = {
                'id': id,
                'solicitud':solicitud.id
                }
            return redirect(reverse(f'formulario_de_pago', kwargs=params)) 

    return render(request, "gestion_de_donaciones/donar.html", data)

def ver_donaciones(request, id) :
    campania = Campania_de_donacion.objects.get(id = id)
    donaciones = Donacion.objects.filter(campania_de_donacion = campania)
    data = {
        "donaciones":donaciones,
    }
    return render(request, "gestion_de_donaciones/ver_donaciones.html",data)