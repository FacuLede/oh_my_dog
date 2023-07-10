from django.shortcuts import render, redirect, reverse
from .forms import CreditCardForm, Pagar
from .models import Tarjeta
from gestion_de_donaciones.models import Solicitud_donacion, Campania_de_donacion, Donacion

# Create your views here.

def validar_tarjeta(form):
    try :
        tarjeta = Tarjeta.objects.get(numero_tarjeta = form['numero_tarjeta'])
        return (tarjeta.cvv == form['cvv'])and(tarjeta.dni_titular == form['dni_titular'] ) 
    except:
        return False
    

def formulario_de_pago(request, id, solicitud):
    form = CreditCardForm()
    data ={
        "form" : form, 
    }
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid() : #and validar_tarjeta(request.POST)

            try :
                tarjeta = Tarjeta.objects.get(numero_tarjeta = request.POST.get('numero_tarjeta'))
                if tarjeta.cvv == request.POST.get('cvv') :
                    if tarjeta.mes_expiracion == int(request.POST.get('mes_expiracion')) and tarjeta.anio_expiracion == int(request.POST.get('anio_expiracion')) :
                        if tarjeta.nombre_titular == request.POST.get('nombre_titular') and tarjeta.apellido_titular == request.POST.get('apellido_titular') and tarjeta.dni_titular == request.POST.get('dni_titular') :
                            params = {
                                'id_campania': id,
                                'id_solicitud':solicitud, 
                                'id_tarjeta':tarjeta.id, 
                            }
                            return redirect(reverse(f'pagar', kwargs=params)) 
                        else:
                            return render(request, 'gestion_de_pagos/formulario_de_pago.html',  {'form': form, "error":"El dni el nombre o el apellido no es válido."})
                    else:
                        return render(request, 'gestion_de_pagos/formulario_de_pago.html',  {'form': form, "error":"La fecha ingresada no es válida."})
                else :
                    return render(request, 'gestion_de_pagos/formulario_de_pago.html',  {'form': form, "error":"La tarjeta o el CVV no son correctos."})
            except:
                return render(request, 'gestion_de_pagos/formulario_de_pago.html',  {'form': form, "error":"Esta tarjeta no es válida."})


        else: 
            return render(request, 'gestion_de_pagos/formulario_de_pago.html', {'form': form, "error":"Alguno de los datos ingresados no es correcto."})
    else:
        form = CreditCardForm()
    
    return render(request, 'gestion_de_pagos/formulario_de_pago.html', data)

def pagar(request, id_campania, id_solicitud, id_tarjeta):
    form = Pagar()
    data = {
        "form" : form,
    }
    campania = Campania_de_donacion.objects.get(id = id_campania)
    solicitud_donacion = Solicitud_donacion.objects.get(id = id_solicitud)
    tarjeta = Tarjeta.objects.get(id = int(id_tarjeta))

    

    if request.method == 'POST' :
        if float(tarjeta.numero_tarjeta) == 4444333322221111 :  #Estas lineas 2 simulan un fallo de conexion
            return render(request, "gestion_de_pagos/pagar.html", {"form":form,"error":"Parece que hubo un fallo de conexión con el sistema, intenta denuevo mas tarde."})
        form = Pagar(request.POST) 
        if form.is_valid()  :
            if tarjeta.saldo >= float(request.POST.get('monto')) :
                tarjeta.saldo = tarjeta.saldo - float(request.POST.get('monto'))
                tarjeta.save() 
                donacion = Donacion()
                donacion.nombre = solicitud_donacion.nombre
                donacion.apellido = solicitud_donacion.apellido
                donacion.email = solicitud_donacion.email
                donacion.monto = float(request.POST.get('monto'))
                donacion.campania_de_donacion = campania
                donacion.save()
                campania.monto_actual = campania.monto_actual + float(request.POST.get('monto') )
                campania.save()
                return render(request, 'gestion_de_pagos/pago_exitoso.html')
            else :
                return render(request, 'gestion_de_pagos/pagar.html', {'form': form, "error":"Tu tarjeta no tiene fondos suficientes."})

    return render(request, "gestion_de_pagos/pagar.html", data)