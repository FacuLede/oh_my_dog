from django.shortcuts import render, redirect
from .forms import Turno_form
from .models import Turno

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
    
    return render(request,"gestion_de_turnos/sacar_turno.html",data)

def turnos_pendientes(request):
    turnos_pendientes=Turno.objects.filter(estado = "Pendiente")
    return render(request,"gestion_de_turnos/turnos_pendientes.html",{"turnos":turnos_pendientes})

def mis_turnos(request):
    mis_turnos=Turno.objects.filter(created_by = request.user)
    return render(request,"gestion_de_turnos/mis_turnos.html",{"turnos":mis_turnos})

def eliminar_turno(request, id):
    if request.user.is_authenticated:
        turno = Turno.objects.get(id=id)
        turno.delete()
        return redirect(to = "mis_turnos")