from django.shortcuts import render, redirect, get_object_or_404
from .models import Paseador, Cuidador
from .forms import Send_email_form, Send_email_logged_form
from django.core.mail import EmailMessage
from .forms import Paseador_form, Cuidador_form
from django.contrib import messages
from django import forms

# Create your views here.

def paseadores (request) :
    if request.user.is_superuser:
        paseadores=Paseador.objects.all()        
    else:
        paseadores=Paseador.objects.filter(visible = True)            
    return render(request,"gestion_de_servicios_prestados/paseadores.html",{"paseadores":paseadores})

def cuidadores (request) :
    if request.user.is_superuser:
        cuidadores=Cuidador.objects.all()        
    else:
        cuidadores=Cuidador.objects.filter(visible = True)        
    
    return render(request,"gestion_de_servicios_prestados/cuidadores.html",{"cuidadores":cuidadores})

def contacto(request, id) :
    mensajes = "No pudes enviarte un mensaje a tí mismo."
    paseador = get_object_or_404(Paseador, id=id)    
    if request.user.is_authenticated and request.user.email != paseador.email :
        form = Send_email_logged_form()
        if request.method == "POST" :
            form = Send_email_logged_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage("¡Oh my dog!",
                                    "Se han contactado contigo por tus servicios como paseador:\n"+
                                    request.POST.get('mensaje')+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    [paseador.email]
                                    )
                mail.send()
                return redirect("home")
        return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
    else :
        form = Send_email_form()
        if not request.user.is_authenticated :
            if request.method == "POST" :
                form = Send_email_form(data=request.POST)
                if form.is_valid() :
                    mail = EmailMessage("¡Oh my dog!",
                                        "Se han contactado contigo por tus servicios como paseador:\n"+
                                        request.POST.get('mensaje')+f"\nDe: {request.POST.get('email')}",
                                        request.POST.get('email'),
                                        [paseador.email]
                                        )
                    mail.send()
                    return redirect("home")
            return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
        else:
            paseadores=Paseador.objects.all()
            return render(request,"gestion_de_servicios_prestados/paseadores.html",{"paseadores":paseadores, "mensajes":mensajes})
    

def contacto_cuidador(request, id) :
    mensajes = "No pudes enviarte un mensaje a tí mismo."
    cuidador = get_object_or_404(Cuidador, id=id)        
    if request.user.is_authenticated and request.user.email != cuidador.email :
        form = Send_email_logged_form()
        if request.method == "POST" :
            form = Send_email_logged_form(data=request.POST)
            if form.is_valid() :
                mail = EmailMessage(f"¡Oh my dog!",
                                    "Se han contactado contigo por tus servicios como cuidador:\n"+
                                    request.POST.get('mensaje')+f"\nDe: {request.user.email}",
                                    request.user.email,
                                    [cuidador.email]
                                    )
                mail.send()
                return redirect("home")
        return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
    else :
        form = Send_email_form()
        if not request.user.is_authenticated :
            if request.method == "POST" :
                form = Send_email_form(data=request.POST)
                if form.is_valid() :
                    mail = EmailMessage(f"¡Oh my dog!",
                                        "Se han contactado contigo por tus servicios como cuidador:\n"+
                                        request.POST.get('mensaje')+f"\nDe: {request.POST.get('email')}",
                                        request.POST.get('email'),
                                        [cuidador.email]
                                        )
                    mail.send()
                    return redirect("home")
            return render(request, "gestion_de_servicios_prestados/contacto.html",{'form':form})
        else:
            cuidadores=Cuidador.objects.all()
            return render(request,"gestion_de_servicios_prestados/cuidadores.html",{"cuidadores":cuidadores, "mensajes":mensajes})

        
def cargar_paseador(request):
    form = Paseador_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Paseador_form(request.POST)
        if form.is_valid() :     
            form.save()    
            data["mensaje"] = "Se agregó al paseador correctamente."  
            return redirect(to="paseadores")
        else :
            data['mensaje_error'] = 'Ya existe un paseador con ese email.' 
    
    return render(request,"gestion_de_servicios_prestados/cargar_paseador.html",data)  

def cargar_cuidador(request):
    form = Cuidador_form()
    data = {
        "form":form
    }
    if request.method ==  'POST':
        form = Cuidador_form(request.POST)
        if form.is_valid() :     
            form.save()    
            data["mensaje"] = "Se agregó al cuidador correctamente."       
            return redirect(to="cuidadores")
        else :
            data['mensaje_error'] = 'Ya existe un cuidador con ese email.'        
    
    return render(request,"gestion_de_servicios_prestados/cargar_cuidador.html",data)  


def editar_paseador(request, id) :    
    if request.user.is_authenticated and request.user.is_superuser :
        paseador = get_object_or_404(Paseador, id=id) 
        form = Paseador_form(request.POST or None, instance = paseador)
        data = {
            'form': form,
        } 
        if form.is_valid():
            paseador.nombre = request.POST['nombre']
            paseador.descripcion = request.POST['descripcion']
            paseador.email = request.POST['email']
            paseador.save()
            return redirect(to = "paseadores") 
        else:
            return render(request,"gestion_de_servicios_prestados/editar_paseador.html",data) 

def editar_cuidador(request, id) :    
    if request.user.is_authenticated and request.user.is_superuser :
        cuidador = get_object_or_404(Cuidador, id=id) 
        form = Cuidador_form(request.POST or None, instance = cuidador)
        data = {
            'form': form,
        } 
        if form.is_valid():
            cuidador.nombre = request.POST['nombre']
            cuidador.descripcion = request.POST['descripcion']
            cuidador.email = request.POST['email']
            cuidador.save()
            return redirect(to = "cuidadores")
        else:
            return render(request,"gestion_de_servicios_prestados/editar_cuidador.html",data) 
        
def eliminar_paseador(request, id):
    if request.user.is_authenticated and request.user.is_superuser :
        paseador = Paseador.objects.get(id=id)
        paseador.delete()
        return redirect(to = "paseadores") 
    
def eliminar_cuidador(request, id):
    if request.user.is_authenticated and request.user.is_superuser :
        cuidador = Cuidador.objects.get(id=id)
        cuidador.delete()
        return redirect(to = "cuidadores") 
    
def ocultar_paseador(request, id):
    if request.user.is_superuser :
        paseador = Paseador.objects.get(id=id)
        paseador.visible = False
        paseador.save()
        return redirect(to = "paseadores") 

def ocultar_cuidador(request, id):
    if request.user.is_superuser :
        cuidador = Cuidador.objects.get(id=id)
        cuidador.visible = False
        cuidador.save()
        return redirect(to = "cuidadores") 

def mostrar_paseador(request, id):
    if request.user.is_superuser :
        paseador = Paseador.objects.get(id=id)
        paseador.visible = True
        paseador.save()
        return redirect(to = "paseadores") 

def mostrar_cuidador(request, id):
    if request.user.is_superuser :
        cuidador = Cuidador.objects.get(id=id)
        cuidador.visible = True
        cuidador.save()
        return redirect(to = "cuidadores") 