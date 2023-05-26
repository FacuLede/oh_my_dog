from django.shortcuts import render, redirect
from .forms import Turno_form
from .models import Turno
from django.db.models import Q

# Create your views here.

def sacar_turno(request):
    turno = Turno()
    form = Turno_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Turno_form(request.POST)
        if form.is_valid() :    
            turno = form.save(commit=False)
            turno.created_by = request.user
            turno.save()        
            # form.save()           
            data["mensaje"] = "Se solicitó el turno correctamente."  
        else :
            data["error"] = "Algo salió mal, inténtalo denuevo."              
    
    return render(request,"gestion_de_turnos/sacar_turno.html",data)

def turnos_pendientes(request):
    turnos_pendientes=Turno.objects.filter(estado = "Pendiente")
    return render(request,"gestion_de_turnos/turnos_pendientes.html",{"turnos":turnos_pendientes})

def mis_turnos(request):
    mis_turnos=Turno.objects.filter(Q(created_by = request.user)&(Q(estado = "Aprobado")|Q(estado = "Pendiente")))
    return render(request,"gestion_de_turnos/mis_turnos.html",{"turnos":mis_turnos})

def eliminar_turno(request, id):
    if request.user.is_authenticated:
        turno = Turno.objects.get(id=id)
        turno.delete()
        return redirect(to = "mis_turnos")
    
def aprobar_turno(request, id):
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        turno.estado = "Aprobado"
        turno.save()
        return redirect(to = "turnos_pendientes")
    
def rechazar_turno(request, id):
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        turno.estado = "Rechazado"
        turno.save()
        return redirect(to = "turnos_pendientes")
    
def cancelar_turno(request, id):
    if request.user.is_superuser:
        turno = Turno.objects.get(id=id)
        turno.estado = "Cancelado"
        turno.save()
        return redirect(to = "turnos_aprobados")
    
def turnos_aprobados(request):
    turnos_pendientes=Turno.objects.filter(estado = "Aprobado")
    return render(request,"gestion_de_turnos/turnos_aprobados.html",{"turnos":turnos_pendientes})
