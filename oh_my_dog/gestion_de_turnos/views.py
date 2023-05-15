from django.shortcuts import render
from .forms import Turno_form

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