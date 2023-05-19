from django.shortcuts import render, redirect, get_object_or_404
from .models import Paseador, Cuidador
from .forms import Send_email_form
from django.core.mail import EmailMessage

# Create your views here.

def paseadores (request) :
    paseadores=Paseador.objects.all()
    return render(request,"gestion_de_servicios_prestados/paseadores.html",{"paseadores":paseadores})

def cuidadores (request) :
    cuidadores=Cuidador.objects.all()
    return render(request,"gestion_de_servicios_prestados/cuidadores.html",{"cuidadores":cuidadores})

def contacto(request, id) :
    mensajes = "No pudes enviarte un mensaje a tí mismo."
    paseador = get_object_or_404(Paseador, id=id)
    form = Send_email_form()
    if request.user.email != paseador.email :
        if request.method == "POST" :
            form = Send_email_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    request.POST.get('mensaje')+f" De: {request.POST.get('email')}",
                                    request.POST.get('email'),
                                    [paseador.email]
                                    )
                # try:
                mail.send()
                return redirect("home")
                # except:
                #     pass
                #     return redirect("home")
        return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
    else :
        paseadores=Paseador.objects.all()
        return render(request,"gestion_de_servicios_prestados/paseadores.html",{"paseadores":paseadores, "mensajes":mensajes})
    

def contacto_cuidador(request, id) :
    mensajes = "No pudes enviarte un mensaje a tí mismo."
    cuidador = get_object_or_404(Cuidador, id=id)    
    form = Send_email_form()
    if request.user.email != cuidador.email :
        if request.method == "POST" :
            form = Send_email_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage(f"¡Oh my dog!",
                                    request.POST.get('mensaje')+f" De: {request.POST.get('email')}",
                                    request.POST.get('email'),
                                    [cuidador.email]
                                    )
                # try:
                mail.send()
                return redirect("home")
                # except:
                #     pass
                #     return redirect("home")
        return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
    else :
        cuidadores=Cuidador.objects.all()
        return render(request,"gestion_de_servicios_prestados/cuidadores.html",{"cuidadores":cuidadores, "mensajes":mensajes})

