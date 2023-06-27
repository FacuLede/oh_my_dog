from django.shortcuts import render, redirect
from .forms import CreditCardForm
from .models import Tarjeta

# Create your views here.

def validar_tarjeta(form):
    try :
        tarjeta = Tarjeta.objects.get(numero_tarjeta = form['numero_tarjeta'])
        return (tarjeta.cvv == form['cvv'])and(tarjeta.dni_titular == form['dni_titular'] ) 
    except:
        return False
    

def formulario_de_pago(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid() and validar_tarjeta(request.POST):
            return redirect(to = 'home') #Eventualmente deberá redirigirte a otro sitio
        else: 
            return render(request, 'gestion_de_pagos/formulario_de_pago.html', {'form': form, "error":"Alguno de los datos ingresados no es correcto."})
    else:
        form = CreditCardForm()
    
    return render(request, 'gestion_de_pagos/formulario_de_pago.html', {'form': form})

