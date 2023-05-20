from django.shortcuts import render
from gestion_de_mascotas.models import Perro_perdido, Perro_en_adopcion, Perro
from .forms import Perro_perdido_form, Perro_en_adopcion_form

# Create your views here.

def perros_perdidos (request) :
    perros_perdidos=Perro_perdido.objects.all()
    return render(request,"gestion_de_mascotas/perros_perdidos.html",{"perros_perdidos":perros_perdidos})

def anunciar_perro_perdido(request):
    form = Perro_perdido_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Perro_perdido_form(request.POST, request.FILES)
        perro_perdido = Perro_perdido()
        if form.is_valid() :     
            perro_perdido = form.save(commit=False)  # Guardar el formulario sin realizar la inserción en la base de datos
            perro_perdido.created_by = request.user.dni   
            perro_perdido.save()  
            print(perro_perdido.created_by)         
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_perdido.html",data)

def perros_en_adopcion (request) :
    perros_en_adopcion=Perro_en_adopcion.objects.all()
    return render(request,"gestion_de_mascotas/perros_en_adopcion.html",{"perros_en_adopcion":perros_en_adopcion})

def anunciar_perro_adopcion(request):
    form = Perro_en_adopcion_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Perro_en_adopcion_form(request.POST, request.FILES)
        if form.is_valid() :            
            form.save()           
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_adopcion.html",data)


def mis_perros (request) :
    mis_perros=Perro.objects.filter(dni_owner = request.user.dni)
    return render(request,"gestion_de_mascotas/mis_perros.html",{"mis_perros":mis_perros})