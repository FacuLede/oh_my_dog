from django.shortcuts import render, redirect, get_object_or_404
from gestion_de_mascotas.models import Perro_perdido, Perro_en_adopcion, Perro, Perro_encontrado
from .forms import Perro_perdido_form, Perro_en_adopcion_form, Send_email_form, Send_email_logged_form, Perro_form, Perro_encontrado_form, Perro_encontrado_update_form, Perro_perdido_update_form
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def perros_perdidos (request) :
    perros_perdidos=Perro_perdido.objects.all()
    return render(request,"gestion_de_mascotas/perros_perdidos.html",{"perros_perdidos":perros_perdidos})

def perros_encontrados (request) :
    perros_encontrados=Perro_encontrado.objects.all()
    return render(request,"gestion_de_mascotas/perros_encontrados.html",{"perros_encontrados":perros_encontrados})

def anunciar_perro_perdido(request):
    perros = list()
    if request.user.is_authenticated :
        perros = Perro.objects.filter(dni_owner = request.user.dni)
    form = Perro_perdido_form()
    data = {
        "form":form,
        "perros":perros,
    }
    if request.method ==  'POST':
        form = Perro_perdido_form(request.POST, request.FILES)
        perro_perdido = Perro_perdido()
        if form.is_valid() :     
            perro_perdido = form.save(commit=False)  # Guardar el formulario sin realizar la inserción en la base de datos
            perro_perdido.created_by = request.user   
            perro_perdido.save()      
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_perdido.html",data)

def anunciar_perro_encontrado(request):
    perros = list()
    if request.user.is_authenticated :
        perros = Perro.objects.filter(dni_owner = request.user.dni)
    form = Perro_encontrado_form()
    data = {
        "form":form,
        "perros":perros,
    }
    if request.method ==  'POST':
        form = Perro_encontrado_form(request.POST, request.FILES)
        perro_encontrado = Perro_encontrado()
        if form.is_valid() :     
            perro_encontrado = form.save(commit=False)
            perro_encontrado.created_by = request.user   
            perro_encontrado.save()      
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_encontrado.html",data)

def perros_en_adopcion (request) :
    # perros_en_adopcion=Perro_en_adopcion.objects.all()
    perros_en_adopcion = Perro_en_adopcion.objects.filter(adoptado = False)
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
            perro_en_adopcion.created_by = request.user         
            perro_en_adopcion.save()
            data["mensaje"] = "Se publicó el anuncio correctamente."              
    
    return render(request,"gestion_de_mascotas/anunciar_perro_adopcion.html",data)

def mis_perros (request) :
    mis_perros=Perro.objects.filter(dni_owner = request.user.dni)
    return render(request,"gestion_de_mascotas/mis_perros.html",{"mis_perros":mis_perros})

def mis_perros_en_adopcion (request) :
    mis_perros_en_adopcion=Perro_en_adopcion.objects.filter(Q(created_by = request.user)&Q(adoptado = False))
    return render(request,"gestion_de_mascotas/mis_perros_en_adopcion.html",{"mis_perros_en_adopcion":mis_perros_en_adopcion})

def eliminar_anuncio_adopcion(request, id):
    if request.user.is_authenticated:
        anuncio = Perro_en_adopcion.objects.get(id=id)
        anuncio.delete()
        # return redirect(to = "mis_perros_en_adopcion")
        return redirect(to = request.META.get('HTTP_REFERER'))
    
def contacto_adopcion(request, id) :
    mensajes = "No puedes enviarte un mensaje a tí mismo."
    publicacion = get_object_or_404(Perro_en_adopcion, id=id)
    autor = get_object_or_404(User, dni=publicacion.created_by.dni)
    
    if request.user.is_authenticated and request.user.email != autor.email :
        form = Send_email_logged_form()
        if request.method == "POST" :
            form = Send_email_logged_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    "Se han contactado contigo por tu publicación de perro en adopción:\n"+
                                    request.POST.get('mensaje')+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    [autor.email]
                                    )
                mail.send()
                return redirect("home")
        return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
    else :
        form = Send_email_form()
        if not request.user.is_authenticated :
            if request.method == "POST" :
                form = Send_email_form(data=request.POST)
                if form.is_valid() :
                    mail = EmailMessage("¡Oh my dog!",
                                        "Se han contactado contigo por tu publicación de perro en adopción:\n"+
                                        request.POST.get('mensaje')+f"\nDe: {request.POST.get('email')}",
                                        request.POST.get('email'),
                                        [autor.email]
                                        )
                    mail.send()
                    return redirect("home")
            return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
        else:
            perros_en_adopcion=Perro_en_adopcion.objects.all()
            return render(request,"gestion_de_mascotas/perros_en_adopcion.html",{"perros_en_adopcion":perros_en_adopcion, "mensajes":mensajes})

def editar_anuncio(request, id) :    
    if request.user.is_authenticated:
        publicacion = get_object_or_404(Perro_en_adopcion, id=id) #obtiene la publicación que se quiere editar
        # current_user = request.user
        form = Perro_en_adopcion_form(request.POST or None, instance = publicacion)
        data = {
            'form': form,
        } 
        if form.is_valid():
            publicacion.titulo = request.POST['titulo']
            publicacion.edad = request.POST['edad']
            publicacion.tamanio = request.POST['tamanio']
            publicacion.detalles_de_salud = request.POST['detalles_de_salud']
            publicacion.zona = request.POST['zona']            
            publicacion.historia = request.POST['historia']
            publicacion.save()
            return redirect(to = "mis_perros_en_adopcion")
        else:
            return render(request,"gestion_de_mascotas/editar_anuncio.html",data)

def cargar_perro(request):
    form = Perro_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Perro_form(request.POST)
        if form.is_valid() :     
            form.save()    
            data["mensaje"] = "Se agregó al perro correctamente."  
        else :
            data['mensaje_error'] = 'Ya existe ese perro.' 
    
    return render(request,"gestion_de_mascotas/cargar_perro.html",data)  

def editar_perro(request, id) :    
    if request.user.is_authenticated and request.user.is_superuser :
        perro = get_object_or_404(Perro, id=id) 
        form = Perro_form(request.POST or None, instance = perro)
        data = {
            'form': form,
        } 
        if form.is_valid():
            perro.nombre = request.POST['nombre']
            perro.edad = request.POST['edad']
            perro.peso = request.POST['peso']
            perro.size = request.POST['size']
            perro.dni_owner = request.POST['dni_owner']
            perro.save()
            return redirect(to = "perros") 
        else:
            return render(request,"gestion_de_mascotas/editar_perro.html",data) 
        
def eliminar_perro(request, id):
    if request.user.is_authenticated and request.user.is_superuser :
        perro = Perro.objects.get(id=id)
        perro.delete()
        return redirect(to = "perros") 
    
def perros (request) :
    perros=Perro.objects.all()
    return render(request,"gestion_de_mascotas/perros.html",{"perros":perros})

def eliminar_anuncio_encontrado(request, id) :
    if request.user.is_authenticated :
        perro = Perro_encontrado.objects.get(id=id)
        perro.delete()
        return redirect(to = "perros_encontrados") 
    
def eliminar_anuncio_perdido(request, id) :
    if request.user.is_authenticated :
        perro = Perro_perdido.objects.get(id=id)
        perro.delete()
        return redirect(to = "perros_perdidos") 

def editar_anuncio_encontrado_2(request, id) :    
    if request.user.is_authenticated:
        publicacion = get_object_or_404(Perro_encontrado, id=id)
        form = Perro_encontrado_update_form(request.POST or None, instance = publicacion)
        data = {
            'form': form,
        } 
        if form.is_valid():
            publicacion.size = request.POST['size']
            publicacion.zona = request.POST['zona']            
            publicacion.descripcion = request.POST['descripcion']
            publicacion.save()
            return redirect(to = "perros_encontrados")
        else:
            return render(request,"gestion_de_mascotas/editar_anuncio_encontrado.html",data)
        
def editar_anuncio_perdido_2(request, id) :    
    if request.user.is_authenticated:
        publicacion = get_object_or_404(Perro_perdido, id=id)
        form = Perro_perdido_update_form(request.POST or None, instance = publicacion)
        data = {
            'form': form,
        } 
        if form.is_valid():    
            if 'nueva_imagen' in request.FILES:
                publicacion.imagen = request.FILES['nueva_imagen']        
            publicacion.size = request.POST['size']
            publicacion.zona = request.POST['zona']            
            publicacion.descripcion = request.POST['descripcion']
            publicacion.nombre = request.POST['nombre']
            publicacion.edad = request.POST['edad']
            publicacion.save()
            return redirect(to = "perros_perdidos")
        else:
            return render(request,"gestion_de_mascotas/editar_anuncio_perdido.html",data)
        
def contacto_encontrado(request, id) :
    mensajes = "No puedes enviarte un mensaje a tí mismo."
    publicacion = get_object_or_404(Perro_encontrado, id=id)
    autor = get_object_or_404(User, dni=publicacion.created_by.dni)
    
    if request.user.is_authenticated and request.user.email != autor.email :
        form = Send_email_logged_form()
        if request.method == "POST" :
            form = Send_email_logged_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    "Se han contactado contigo por tu publicación de un perro encontrado:\n"+
                                    request.POST.get('mensaje')+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    [autor.email]
                                    )
                mail.send()
                return redirect("home")
        return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
    else :
        form = Send_email_form()
        if not request.user.is_authenticated :
            if request.method == "POST" :
                form = Send_email_form(data=request.POST)
                if form.is_valid() :
                    mail = EmailMessage("¡Oh my dog!",
                                        "Se han contactado contigo por tu publicación de un perro encontrado:\n"+
                                        request.POST.get('mensaje')+f"\nDe: {request.POST.get('email')}",
                                        request.POST.get('email'),
                                        [autor.email]
                                        )
                    mail.send()
                    return redirect("home")
            return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
        else:
            perros_encontrados=Perro_encontrado.objects.all()
            return render(request,"gestion_de_mascotas/perros_adopcion.html",{"perros_encontrados":perros_encontrados, "mensajes":mensajes})

def contacto_perdido(request, id) :
    mensajes = "No puedes enviarte un mensaje a tí mismo."
    publicacion = get_object_or_404(Perro_perdido, id=id)
    autor = get_object_or_404(User, dni=publicacion.created_by.dni)
    
    if request.user.is_authenticated and request.user.email != autor.email :
        form = Send_email_logged_form()
        if request.method == "POST" :
            form = Send_email_logged_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    "Se han contactado contigo por tu publicación de un perro perdido:\n"+
                                    request.POST.get('mensaje')+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    [autor.email]
                                    )
                mail.send()
                return redirect("home")
        return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
    else :
        form = Send_email_form()
        if not request.user.is_authenticated :
            if request.method == "POST" :
                form = Send_email_form(data=request.POST)
                if form.is_valid() :
                    mail = EmailMessage("¡Oh my dog!",
                                        "Se han contactado contigo por tu publicación de un perro perdido:\n"+
                                        request.POST.get('mensaje')+f"\nDe: {request.POST.get('email')}",
                                        request.POST.get('email'),
                                        [autor.email]
                                        )
                    mail.send()
                    return redirect("home")
            return render(request, "gestion_de_mascotas/contacto_adopcion.html",{'form':form})
        else:
            perros_perdidos=Perro_perdido.objects.all()
            return render(request,"gestion_de_mascotas/perros_perdidos.html",{"perros_perdidos":perros_perdidos, "mensajes":mensajes})
        
def editar_anuncio_perdido(request, id):
    publicacion = get_object_or_404(Perro_perdido, pk=id)
    
    if request.method == 'POST':
        form = Perro_perdido_update_form(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            if request.POST['nueva_imagen'] != "":
                publicacion.imagen = "perros_perdidos/"+request.POST['nueva_imagen']
            publicacion.size = request.POST['size']
            publicacion.zona = request.POST['zona']            
            publicacion.descripcion = request.POST['descripcion']
            publicacion.nombre = request.POST['nombre']
            publicacion.edad = request.POST['edad']
            publicacion.save()
            return redirect('perros_perdidos')
    else:
        form = Perro_perdido_update_form(instance=publicacion)

    return render(request, 'gestion_de_mascotas/editar_anuncio_perdido.html', {'form': form})

def editar_anuncio_encontrado(request, id):
    publicacion = get_object_or_404(Perro_encontrado, pk=id)
    
    if request.method == 'POST':
        form = Perro_encontrado_update_form(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            if request.POST['nueva_imagen'] != "":
                publicacion.imagen = "perros_encontrados/"+request.POST['nueva_imagen']

            # publicacion.fecha_encontrado = form.cleaned_data['fecha_encontrado']

            publicacion.size = request.POST['size']
            publicacion.zona = request.POST['zona']            
            publicacion.descripcion = request.POST['descripcion']
            publicacion.save()
            return redirect('perros_encontrados')
    else:
        form = Perro_encontrado_update_form(instance=publicacion)

    return render(request, 'gestion_de_mascotas/editar_anuncio_perdido.html', {'form': form})

def adopcion_realizada(request, id):
    if request.user.is_authenticated:
        perro = Perro_en_adopcion.objects.get(id=id)
        perro.adoptado = True
        perro.save()
        # return HttpResponseRedirect(request.get_full_path())
        # print()
        return redirect(to = request.META.get('HTTP_REFERER'))  #request.META.get('HTTP_REFERER') devuelve la anterior vista ejecutada