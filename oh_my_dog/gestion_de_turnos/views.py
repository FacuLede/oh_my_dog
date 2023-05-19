from django.shortcuts import render
from .forms import Turno_form
from .models import Turno

# Create your views here.

def sacar_turno(request):
    form = Turno_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Turno_form(request.POST)
        if form.is_valid() :            
            form.save()           
            data["mensaje"] = "Se solicitó el turno correctamente."              
    
    return render(request,"gestion_de_turnos/sacar_turno.html",data)

def turnos_pendientes(request):
    turnos_pendientes=Turno.objects.filter(estado = "Pendiente")
    return render(request,"gestion_de_turnos/turnos_pendientes.html",{"turnos":turnos_pendientes})