from django.shortcuts import render, redirect, get_object_or_404
from .forms import Turno_form, Reprogramar_turno_form, Turno_form_perroless
from .models import Turno
from django.db.models import Q
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from gestion_de_mascotas.models import Perro

# Create your views here.

def sacar_turno(request):
    turno = Turno()
    if Perro.objects.filter(owner = request.user).count() != 0 :
        form = Turno_form(request.user)
    else:
        form = Turno_form_perroless()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        if Perro.objects.filter(owner = request.user).count() != 0 :
            form = Turno_form(request.user,request.POST)
        else:
            form = Turno_form_perroless(request.POST)
        if form.is_valid() :    
            turno = form.save(commit=False) 
            if turno.perro is not None :   
                if turno.motivo.servicio == "Castración" or turno.motivo.servicio == "Desparasitación" :
                    turnos = Turno.objects.filter(Q(perro = turno.perro)&Q(motivo = turno.motivo))
                    if turnos.count() != 0 :
                        return render(request,"gestion_de_turnos/sacar_turno.html",{"form":form, "error":"Ya has solicitado un turno similar."})
            
            else:    
                turnos_2 = Turno.objects.filter(Q(perro = None)&Q(created_by = request.user)&Q(motivo = turno.motivo)&Q(fecha = turno.fecha)&Q(franja_horaria = turno.franja_horaria))
                if turnos_2.count() != 0 :
                    return render(request,"gestion_de_turnos/sacar_turno.html",{"form":form, "error":"Ya has solicitado un turno similar."})
            turno.created_by = request.user
            turno.save()  
            data["mensaje"] = "Se solicitó el turno correctamente."   
        else :
            data["error"] = "No se pudo solicitar el turno."  
            print(form.errors)            
    
    return render(request,"gestion_de_turnos/sacar_turno.html",data)

def turnos_pendientes(request):
    turnos_pendientes=Turno.objects.filter(estado = "Pendiente")
    return render(request,"gestion_de_turnos/turnos_pendientes.html",{"turnos":turnos_pendientes})

def mis_turnos(request):
    mis_turnos=Turno.objects.filter(Q(created_by = request.user)&(Q(estado = "Aprobado")|Q(estado = "Pendiente")))
    return render(request,"gestion_de_turnos/mis_turnos.html",{"turnos":mis_turnos})

def eliminar_turno(request, id, motivo):
    if request.user.is_authenticated:
        turno = Turno.objects.get(id=id)
        autor = get_object_or_404(User, dni=turno.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"El cliente {request.user.username} ha cancelado su turno para el día {turno.fecha} en la franja horaria {turno.franja_horaria}.\n"+
                                    "Motivo: "+motivo+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    ["ohmydog.veterinaria.123@gmail.com"] #Utiliza el email del autor del turno
                                    )
        mail.send()
        turno.delete()
        return redirect(to = "mis_turnos")
    
def aprobar_turno(request, id):
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        autor = get_object_or_404(User, dni=turno.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"Se ha aprobado tu turno del día {turno.fecha} en la franja horaria {turno.franja_horaria}.\n"
                                    "\nDe: ohmydog.veterinaria.123@gmail.com",
                                    "ohmydog.veterinaria.123@gmail.com",
                                    [autor.email] #Utiliza el email del autor del turno
                                    )
        mail.send()
        turno.estado = "Aprobado"
        turno.save()
        return redirect(to = "turnos_pendientes")
    
def rechazar_turno_v1(request, id):
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        autor = get_object_or_404(User, dni=turno.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"Lo sentimos, lamentablemente no habían turnos disponibles para el día {turno.fecha} en la franja horaria {turno.franja_horaria}.\n"
                                    +"Su turno fue rechazado."+"\nDe: ohmydog.veterinaria.123@gmail.com",
                                    "ohmydog.veterinaria.123@gmail.com",
                                    [autor.email] #Utiliza el email del autor del turno
                                    )
        mail.send()
        turno.estado = "Rechazado"
        turno.save()
        return redirect(to = "turnos_pendientes")
    
def rechazar_turno(request, id, motivo):
    #El motivo se debe enviar por email
    print(motivo)
    if request.user.is_superuser:
        publicacion = get_object_or_404(Turno, id=id)    #Recupera el turno con la id recibida
        autor = get_object_or_404(User, dni=publicacion.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"Se ha rechazado tu turno para el día {publicacion.fecha} en la franja horaria {publicacion.franja_horaria}.\n"+
                                    "Motivo: "+motivo+f"\nDe: ohmydog.veterinaria.123@gmail.com",
                                    "ohmydog.veterinaria.123@gmail.com",
                                    [autor.email] #Utiliza el email del autor del turno
                                    )
        mail.send()
        turno = Turno.objects.get(id=id)
        turno.estado = "Rechazado"
        turno.save()
        return redirect(to = "turnos_pendientes")
    
def cancelar_turno(request, id):
    """Ya no se usa
    """
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        turno.estado = "Cancelado"
        turno.save()
        return redirect(to = "turnos_aprobados")
    
def cancelar_turno_aprobado(request, id, motivo):
    #El motivo se debe enviar por email
    print(motivo)
    if request.user.is_superuser:
        publicacion = get_object_or_404(Turno, id=id)    #Recupera el turno con la id recibida
        autor = get_object_or_404(User, dni=publicacion.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"Se ha cancelado tu turno del día {publicacion.fecha} en la franja horaria {publicacion.franja_horaria}.\n"+
                                    "Motivo: "+motivo+f"\nDe: ohmydog.veterinaria.123@gmail.com",
                                    "ohmydog.veterinaria.123@gmail.com",
                                    [autor.email] #Utiliza el email del autor del turno
                                    )
        mail.send()
        turno = Turno.objects.get(id=id)
        turno.estado = "Cancelado"
        turno.save()
        return redirect(to = "turnos_aprobados")
    
def turnos_aprobados(request):
    turnos_pendientes=Turno.objects.filter(estado = "Aprobado")
    return render(request,"gestion_de_turnos/turnos_aprobados.html",{"turnos":turnos_pendientes})

def reprogramar_turno_aprobado(request, id): 
    turno = get_object_or_404(Turno, id=id) #obtiene el turno que se quiere reprogramar
    form = Reprogramar_turno_form(request.POST or None, instance = turno)
    data = {
        'form': form,
    } 
    if form.is_valid():
        turno.save()
        autor = get_object_or_404(User, dni=turno.created_by.dni) #Recupera el autor del turno 
        mail = EmailMessage("¡Oh my dog!",
                                    f"Se ha reprogramado tu turno para el día {turno.fecha} en la franja horaria {turno.franja_horaria}.\n"+
                                    "Motivo: "+request.POST['motivo']+f"\nDe: ohmydog.veterinaria.123@gmail.com",
                                    "ohmydog.veterinaria.123@gmail.com",
                                    [autor.email] #Utiliza el email del autor del turno
                                    )
        mail.send()
        return redirect(to = "turnos_aprobados")                
    else:
        return render(request,"gestion_de_turnos/reprogramar_turno.html",data)