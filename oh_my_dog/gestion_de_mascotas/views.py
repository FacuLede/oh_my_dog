from django.shortcuts import render, redirect, get_object_or_404
from gestion_de_mascotas.models import Perro_perdido, Perro_en_adopcion, Perro
from .forms import Perro_perdido_form, Perro_en_adopcion_form, Send_email_form
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
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
    perros = list()
    if request.user.is_authenticated :
        perros = Perro.objects.filter(dni_owner = request.user.dni)
        
    perro_en_adopcion = Perro_en_adopcion() 
    form = Perro_en_adopcion_form()
    data = {
        "form":form,
        "perros":perros,
    }
    if request.method ==  'POST':
        form = Perro_en_adopcion_form(request.POST, request.FILES)
        if form.is_valid() :   
            perro_en_adopcion = form.save(commit=False)
            perro_en_adopcion.created_by = request.user.dni         
            perro_en_adopcion.save()
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_adopcion.html",data)
    # else :
    #     return redirect(to='home')


def mis_perros (request) :
    mis_perros=Perro.objects.filter(dni_owner = request.user.dni)
    return render(request,"gestion_de_mascotas/mis_perros.html",{"mis_perros":mis_perros})

def mis_perros_en_adopcion (request) :
    mis_perros_en_adopcion=Perro_en_adopcion.objects.filter(created_by = request.user.dni)
    return render(request,"gestion_de_mascotas/mis_perros_en_adopcion.html",{"mis_perros_en_adopcion":mis_perros_en_adopcion})


def eliminar_anuncio_adopcion(request, id):
    if request.user.is_authenticated:
        turno = Perro_en_adopcion.objects.get(id=id)
        turno.delete()
        return redirect(to = "mis_perros_en_adopcion")
    
def contacto_adopcion(request, id) :
    mensajes = "No pudes enviarte un mensaje a tí mismo."
    publicacion = get_object_or_404(Perro_en_adopcion, id=id)
    autor = get_object_or_404(User, dni=publicacion.created_by)
    form = Send_email_form()
    if request.user.email != autor.email :
        if request.method == "POST" :
            form = Send_email_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    request.POST.get('mensaje')+f" De: {request.POST.get('email')}",
                                    request.POST.get('email'),
                                    [autor.email]
                                    )
                # try:
                mail.send()
                return redirect("home")
                # except:
                #     pass
                #     return redirect("home")
        return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
    else :
        # paseadores=Paseador.objects.all()
        # return render(request,"gestion_de_servicios_prestados/paseadores.html",{"paseadores":paseadores, "mensajes":mensajes})
        perros_en_adopcion=Perro_en_adopcion.objects.all()
        return render(request,"gestion_de_mascotas/perros_en_adopcion.html",{"perros_en_adopcion":perros_en_adopcion, "mensajes":mensajes})

def editar_anuncio(request, id) :

    """
    Implementación alternativa de la función editar_perfil
    """
    
    if request.user.is_authenticated:
        publicacion = get_object_or_404(Perro_en_adopcion, id=id) #obtiene la publicación que se quiere editar
        # current_user = request.user
        form = Perro_en_adopcion_form(request.POST or None, instance = publicacion)
        data = {
            'form': form,
        } 
        if form.is_valid():
            publicacion.edad = request.POST['edad']
            publicacion.descripcion = request.POST['descripcion']
            publicacion.localidad = request.POST['localidad']
            publicacion.save()
            return redirect(to = "mis_perros_en_adopcion")
        else:
            return render(request,"gestion_de_mascotas/editar_anuncio.html",data)