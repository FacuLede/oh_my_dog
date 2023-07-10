from django.shortcuts import render, redirect, get_object_or_404, reverse
from gestion_de_mascotas.models import Perro_perdido, Perro_en_adopcion, Perro, Perro_encontrado, Entrada, Libreta_sanitaria, Registro_vacuna, Servicio_veterinario, Vacuna
from .forms import Perro_perdido_form, Perro_en_adopcion_form, Send_email_form, Send_email_logged_form, Perro_form, Perro_encontrado_form, Perro_encontrado_update_form, Perro_perdido_update_form, Perro_form_update, Entrada_form, Entrada_form_vacuna
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import date
# Create your views here.

def perros_perdidos (request) :
    perros_perdidos=Perro_perdido.objects.all()
    return render(request,"gestion_de_mascotas/perros_perdidos.html",{"perros_perdidos":perros_perdidos})

def perros_encontrados (request) :
    perros_encontrados=Perro_encontrado.objects.all()
    return render(request,"gestion_de_mascotas/perros_encontrados.html",{"perros_encontrados":perros_encontrados})

def anunciar_perro_perdido(request):  
    perros = list()
    if (request.user.is_authenticated) :  
        perros = Perro.objects.filter(owner = request.user)

    form = Perro_perdido_form()
    ok = True #Esta variable se le envía en el data al docuemnto html para dependiendo de su valor mostrar o uno un botón
    data = {
        "form":form,
        "perros":perros,
        "ok":ok,
    }

    if request.method ==  'POST':
        form = Perro_perdido_form(request.POST, request.FILES)
        perro_perdido = Perro_perdido()
        if form.is_valid() :     
            perro_perdido = form.save(commit=False)  # Guardar el formulario sin realizar la inserción en la base de datos
            perro_perdido.created_by = request.user   
            perro_perdido.save()      
            data["mensaje"] = "Se publicó el anuncio correctamente."  
            return redirect(to="perros_perdidos")            
    
    return render(request,"gestion_de_mascotas/anunciar_perro_perdido.html",data)

def id_valida(request, id):
    """Esta función garantiza que la id corresponde un perro perteneciente 
    al usuario actual, para que no se pueda setear los datos de un perro que 
    no le corresponde através de la url
    """
    perros = Perro.objects.filter(owner = request.user)
    for perro in perros :
        if int(perro.id) == int(id) :
            return True
    return False

def cargar_datos_perro(request, id):
    perros = Perro.objects.filter(owner = request.user)

    if id_valida(request, id ):  
        ok = False
        perro = get_object_or_404(Perro, id=int(id))       
        datos_iniciales = {
            'nombre': perro.nombre,
            'size':perro.size,
            'sexo':perro.sexo,
            'raza':perro.raza,
        }
        form = Perro_perdido_form(initial=datos_iniciales)   
        data = {
            "form":form,
            "perros":perros,
            "ok":ok,
        }
    else:
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
            return redirect(to="perros_perdidos")   
    
    return render(request,"gestion_de_mascotas/anunciar_perro_perdido.html",data)    

def anunciar_perro_encontrado(request):
    perros = list()
    if request.user.is_authenticated :
        perros = Perro.objects.filter(owner = request.user)
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
            return redirect(to="perros_encontrados")             
    
    return render(request,"gestion_de_mascotas/anunciar_perro_encontrado.html",data)

def perros_en_adopcion (request) :
    perros_en_adopcion=Perro_en_adopcion.objects.all()
    # perros_en_adopcion = Perro_en_adopcion.objects.filter(adoptado = False)
    return render(request,"gestion_de_mascotas/perros_en_adopcion.html",{"perros_en_adopcion":perros_en_adopcion})

def anunciar_perro_adopcion(request):
    perros = list()
    if request.user.is_authenticated :
        perros = Perro.objects.filter(owner = request.user)
        
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
            return redirect(to="perros_en_adopcion")           
    
    return render(request,"gestion_de_mascotas/anunciar_perro_adopcion.html",data)

def mis_perros (request) :
    mis_perros=Perro.objects.filter(owner = request.user)
    return render(request,"gestion_de_mascotas/mis_perros.html",{"mis_perros":mis_perros})

def mis_perros_en_adopcion (request) :
    mis_perros_en_adopcion=Perro_en_adopcion.objects.filter(created_by = request.user)
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

def editar_anuncio(request, id, type) :    
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
            if type == 'all' :
                return redirect(to = "perros_en_adopcion")
            else :
                return redirect(to = "mis_perros_en_adopcion")
        else:
            return render(request,"gestion_de_mascotas/editar_anuncio.html",data)

def validar_perro(request, perros):
    for p in perros :
        if p.nombre == request.POST['nombre']:
            return False
    return True

def cargar_perro(request, id):
    owner = get_object_or_404(User, id=id)
    perros = Perro.objects.filter(owner = owner)
    form = Perro_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Perro_form(request.POST)
        if form.is_valid() and validar_perro(request, perros):               
            perro = form.save(commit=False)
            perro.owner = owner        
            perro.save()
            libreta_sanitaria = Libreta_sanitaria()
            libreta_sanitaria.perro = perro
            libreta_sanitaria.save()
            data["mensaje"] = "Se agregó al perro correctamente."  
            params = {'id': id}
            return redirect(reverse(f'ver_perros_cliente', kwargs=params)) 
        else :
            data['mensaje_error'] = 'Ya existe ese perro.' 
    
    return render(request,"gestion_de_mascotas/cargar_perro.html",data)  

def editar_perro(request, id) :    
    if request.user.is_authenticated and request.user.is_superuser :
        perro = get_object_or_404(Perro, id=id)
        form = Perro_form_update(request.POST or None, instance = perro)
        data = {
            'form': form,
        } 
        if form.is_valid():
            perro.nombre = request.POST['nombre']
            perro.size = request.POST['size']
            perro.save()
            params = {'id': perro.owner.id}
            return redirect(reverse(f'ver_perros_cliente', kwargs=params)) 
        else:
            return render(request,"gestion_de_mascotas/editar_perro.html",data) 
        
def eliminar_perro(request,id2, id):
    if request.user.is_authenticated and request.user.is_superuser :
        perro = Perro.objects.get(id=id)
        perro.delete()        
        return redirect(to = request.META.get('HTTP_REFERER'))
    
def perros (request) :
    perros=Perro.objects.all()
    return render(request,"gestion_de_mascotas/perros.html",{"perros":perros})

def eliminar_anuncio_encontrado(request, id) :
    if request.user.is_authenticated :
        perro = Perro_encontrado.objects.get(id=id)
        perro.delete()
        return redirect(to = request.META.get('HTTP_REFERER'))
    
def eliminar_anuncio_perdido(request, id) :
    if request.user.is_authenticated :
        perro = Perro_perdido.objects.get(id=id)
        perro.delete()
        return redirect(to = request.META.get('HTTP_REFERER'))            

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

        
def editar_anuncio_perdido(request, id, type):
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
            publicacion.sexo = request.POST['sexo']
            publicacion.franja_horaria = request.POST['franja_horaria']
            publicacion.save()
            # return redirect('perros_perdidos')
            if type == 'all' :
                return redirect(to = "perros_perdidos")
            else :
                return redirect(to = "mis_perros_perdidos")
    else:
        form = Perro_perdido_update_form(instance=publicacion)

    return render(request, 'gestion_de_mascotas/editar_anuncio_perdido.html', {'form': form})

def editar_anuncio_encontrado(request, id, type):
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
            if type == 'all' :
                return redirect(to = "perros_encontrados")
            else :
                return redirect(to = "mis_perros_encontrados")
    else:
        form = Perro_encontrado_update_form(instance=publicacion)

    return render(request, 'gestion_de_mascotas/editar_anuncio_perdido.html', {'form': form})

def adopcion_realizada(request, id):
    if request.user.is_authenticated:
        perro = Perro_en_adopcion.objects.get(id=id)
        perro.adoptado = True
        perro.save()
        return redirect(to = request.META.get('HTTP_REFERER'))  #request.META.get('HTTP_REFERER') devuelve la anterior vista ejecutada

def perro_encontrado(request, id):
    if request.user.is_authenticated:
        perro = Perro_perdido.objects.get(id=id)
        perro.encontrado = True
        perro.save()
        return redirect(to = request.META.get('HTTP_REFERER'))  #request.META.get('HTTP_REFERER') devuelve la anterior vista ejecutada
    
def owner_encontrado(request, id):
    if request.user.is_authenticated:
        perro = Perro_encontrado.objects.get(id=id)
        perro.recuperado = True
        perro.save()
        return redirect(to = request.META.get('HTTP_REFERER'))  #request.META.get('HTTP_REFERER') devuelve la anterior vista ejecutada

def mis_perros_perdidos(request):
    mis_perros_perdidos = Perro_perdido.objects.filter(created_by = request.user)
    mis_perros_perdidos = mis_perros_perdidos.reverse()
    return render(request,"gestion_de_mascotas/mis_perros_perdidos.html",{'mis_perros_perdidos':mis_perros_perdidos})

def mis_perros_encontrados(request):
    mis_perros_encontrados = Perro_encontrado.objects.filter(created_by = request.user)
    return render(request,"gestion_de_mascotas/mis_perros_encontrados.html",{'mis_perros_encontrados':mis_perros_encontrados})

def ver_perros_cliente(request, id):
    perro_owner = User.objects.get(id=id)
    perros_cliete = Perro.objects.filter(owner = perro_owner)
    return render(request,"gestion_de_mascotas/perros_cliente.html",{'perros':perros_cliete, "cliente":perro_owner})

def ver_historial_medico(request, id):
    """
    Se recibe la id de un perro
    """
    perro = Perro.objects.get(id=id)
    entradas = Entrada.objects.filter(perro = perro) #Filtra las entradas del perro
    return render(request,"gestion_de_mascotas/historial_medico.html",{'entradas':entradas, 'id_perro':id, 'id_user':perro.owner.id})

def crear_entrada(request, id):
    perro = Perro.objects.get(id=id)
    libreta = Libreta_sanitaria.objects.get(perro = perro)
    form = Entrada_form(libreta.castrado)
    data = {
        "form":form,
        "id":id,
    }
    if request.method ==  'POST':
        
        form = Entrada_form(libreta.castrado,request.POST, request.FILES)
        if form.is_valid() :               
            servicio = Servicio_veterinario.objects.get(id = request.POST.get('motivo'))
            if servicio.servicio == "Castración" :
                libreta.castrado = True
                libreta.save()
            elif servicio.servicio == "Desparasitación" :                
                libreta.ultima_desparasitacion = date.today()
                libreta.save()
            elif servicio.servicio == "Vacunación" :
                registro_vacuna = Registro_vacuna()
                registro_vacuna.perro = Perro.objects.get(id = id)
                from gestion_de_mascotas.models import Vacuna
                registro_vacuna.vacuna = Vacuna.objects.get(id = int(request.POST.get('vacuna')))
                registro_vacuna.numero_dosis = int(request.POST.get('numero_dosis'))
                registro_vacuna.save()                
            entrada = form.save(commit=False)
            entrada.perro = perro       
            entrada.save()             
            params = {'id': id}
            return redirect(reverse(f'ver_historial_medico', kwargs=params)) 
        else:
            if int(request.POST.get('peso')) < 0 :
                data['mensaje_error'] = "El peso debe ser un valor positivo."
            elif int(request.POST.get('numero_dosis')) < 0 :
                data['mensaje_error'] = "El número de dosis no puede ser negativo."
            else:                
                data['mensaje_error'] = "Los campos dosis y vacuna son obligatorios para vacunación."    
    return render(request,"gestion_de_mascotas/crear_entrada.html",data)

def eliminar_entrada(request,id2, id) :
    if request.user.is_superuser :
        entrada = Entrada.objects.get(id=id)
        entrada.delete()
        return redirect(to = request.META.get('HTTP_REFERER'))     

def editar_entrada(request, id) :    
    from .forms import Entrada_update_form, Entrada_update_form_vacunacion
    entrada = Entrada.objects.get(id=id)
    if entrada.motivo.servicio == "Vacunación":
        form = Entrada_update_form_vacunacion(request.POST or None, instance = entrada)    
    else:
        form = Entrada_update_form(request.POST or None, instance = entrada)    
    if form.is_valid():            
        # entrada_2 = form.save(commit=False)
        # from gestion_de_mascotas.models import Vacuna
        # entrada_2.vacuna = Vacuna.objects.get(request.POST.get('vacuna'))    
        form.save()
        params = {'id': entrada.perro.id}
        return redirect(reverse(f'ver_historial_medico', kwargs=params)) 
    else:
        print(form.errors)
        data = {
            'form': form,
        } 
        return render(request,"gestion_de_mascotas/editar_entrada.html",data)            
    
def ver_libreta_sanitaria(request, id) :
    perro = Perro.objects.get(id = id)
    libreta_sanitaria = Libreta_sanitaria.objects.get(perro = perro)
    vacunas_registradas = Registro_vacuna.objects.filter(perro = perro)
    data = {
        "perro":perro, 
        "libreta_sanitaria":libreta_sanitaria,
        "vacunas":vacunas_registradas,
    }
    return render(request,"gestion_de_mascotas/libreta_sanitaria.html",data)


def elegir_motivo(request, id) :
    perro = Perro.objects.get(id = id)
    libreta_sanitaria = Libreta_sanitaria.objects.get(perro = perro)

    if libreta_sanitaria.castrado :
        motivos = Servicio_veterinario.objects.exclude(servicio = "Castración")
    else :
        motivos = Servicio_veterinario.objects.all()

    data = {
        "motivos":motivos,        
    }

    if request.method == 'POST' :
        
        if request.POST.get('motivo') != "" :
            #Si el formulario es válido se evalúa que hacer en función del motivo elegido
            print(request.POST.get('motivo'))
            motivo = Servicio_veterinario.objects.get(id = request.POST.get('motivo'))
            if motivo.servicio != "Vacunación" :
                params = {
                    'id': id,
                    'motivo':request.POST.get('motivo')
                }
                return redirect(reverse(f'agregar_entrada', kwargs=params)) 
            else:
                params = {
                    'id': id,
                    'motivo':request.POST.get('motivo')
                }
                return redirect(reverse(f'agregar_entrada_vacuna', kwargs=params)) 
        else:
            data['mensaje_error'] = "Debes elegir un motivo."
            
    return render(request, "gestion_de_mascotas/elegir_motivo.html", data)

def agregar_entrada(request, id, motivo): #Recibe la id de un perro y debería recibir un motivo
    perro = Perro.objects.get(id=id)
    libreta_sanitaria = Libreta_sanitaria.objects.get(perro = perro)
    form = Entrada_form()
    data = {
        "form":form,
        "id":id,
    }
    if request.method ==  'POST':        
        form = Entrada_form(request.POST, request.FILES)
        if form.is_valid() :               
            servicio = Servicio_veterinario.objects.get(id = int(motivo))
            entrada = form.save(commit=False)
            entrada.motivo = servicio

            if servicio.servicio == "Castración" :
                libreta_sanitaria.castrado = True
                libreta_sanitaria.save()
            elif servicio.servicio == "Desparasitación" :                
                libreta_sanitaria.ultima_desparasitacion = date.today()
                libreta_sanitaria.save()
            
            entrada.perro = perro       
            entrada.save()       
            data['mensaje'] = "Salió bien."      
            params = {'id': id}
            return redirect(reverse(f'ver_historial_medico', kwargs=params)) 
        else:
            return render(request,"gestion_de_mascotas/crear_entrada.html",{"form":form, "id":id})
    return render(request,"gestion_de_mascotas/crear_entrada.html",data)

def agregar_entrada_vacuna(request, id, motivo) :
    perro = Perro.objects.get(id=id)
    form = Entrada_form_vacuna()
    data = {
        "form":form,
        "id":id,
    }
    if request.method ==  'POST':        
        form = Entrada_form_vacuna(request.POST, request.FILES)
        if form.is_valid() :    
            servicio = Servicio_veterinario.objects.get(id = int(motivo))
            entrada = form.save(commit=False)
            entrada.motivo = servicio

            registro_vacuna = Registro_vacuna()
            registro_vacuna.perro = perro
            registro_vacuna.vacuna = Vacuna.objects.get(id = int(request.POST.get('vacuna')))
            registro_vacuna.numero_dosis = int(request.POST.get('numero_dosis'))
            registro_vacuna.save()  

            entrada.perro = perro       
            entrada.save()  

            params = {'id': id}
            return redirect(reverse(f'ver_historial_medico', kwargs=params)) 
        else:
            # if form.errors:
            #     data['mensaje_error'] = []
            #     error_peso = form.errors.get("peso", None)
            #     if error_peso:
            #         error_peso = error_peso.as_data()[0].message
            #         data["mensaje_error"].append(error_peso)
            #     error_numero_dosis = form.errors.get("numero_dosis", None)
            #     if error_numero_dosis:
            #         error_numero_dosis = error_numero_dosis.as_data()[0].message
            #         data["mensaje_error"].append(error_numero_dosis)
            return render(request,"gestion_de_mascotas/crear_entrada.html",{"form":form, "id":id})

    return render(request,"gestion_de_mascotas/crear_entrada.html",data)
    #Entrada_form_vacuna