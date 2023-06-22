from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def clientes2 (request) :
    print(request.GET.get("search"))
    clientes = User.objects.filter(is_superuser=False)        
    return render(request,"gestion_de_clientes/clientes.html",{"clientes":clientes})

def clientes(request):
    search_query = request.GET.get("search")
    clientes = User.objects.filter(is_superuser=False)
    
    if request.method == "GET" and "search" in request.GET:
        print("Entra")
        if search_query:
            clientes = clientes.filter(username__icontains=search_query)
    
    context = {
        "clientes": clientes,
        "search_query": search_query
    }
    
    return render(request, "gestion_de_clientes/clientes.html", context)