from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UserUpdateForm

# Create your views here.

def home (request) :
    return render(request, 'gestion_de_usuarios/home.html')

def iniciar_sesion (request) :
    if request.method == 'POST' :
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid() :
            username1 = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password")
            user = authenticate(username=username1, password = password1)
            if user is not None :
                login(request,user)
                return redirect('home')
            else:
                # messages.error(request,"Alguno de los datos ingresados no es correcto.")
                pass
        else:
            messages.error(request,"Alguno de los datos ingresados no es correcto.")
            
    form = AuthenticationForm()
    return render(request, "gestion_de_usuarios/iniciar_sesion.html",{"form":form})
    # return render(request, 'gestion_de_usuarios/iniciar_sesion.html')

def registrarse (request) :
    return render(request, 'gestion_de_usuarios/registrarse.html')

def cerrar_sesion(request) :
    logout(request)
    return redirect('home')

class UserRegisterForm(UserCreationForm) : #No se guarda el dni en la base de datos
    email = forms.EmailField()
    dni = forms.CharField(max_length=8)
    class Meta:
        model = User
        fields = ('username','email','dni','password1','password2')

class Registrarse(View) :
    
    def get(self, request):
        form = UserRegisterForm()
        # form = UserCreationForm()
        return render(request, "gestion_de_usuarios/registrarse.html",{"form":form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) 
            return redirect('home')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
            return render(request, "gestion_de_usuarios/registrarse.html",{"form":form})
        

def perfil(request):
    usuario=request.user
    return render(request,"gestion_de_usuarios/perfil_usuario.html",{"usuario":usuario})

def editar_perfil_2(request) :
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UserUpdateForm(request.POST or None, instance = current_user)
        data = {
            'form': form,
        } 
        if form.is_valid():
            print(request.POST)
            form.save()
            login(request,current_user)
            return redirect(to = "perfil")
        else:
            return render(request,"gestion_de_usuarios/editar_perfil.html",data)
        

def editar_perfil(request) :

    """
    Implementación alternativa de la función editar_perfil
    """
    if request.user.is_authenticated:
        current_user = request.user
        form = UserUpdateForm(request.POST or None, instance = current_user)
        data = {
            'form': form,
        } 
        if form.is_valid():
            current_user.username = request.POST['username']
            current_user.email = request.POST['email']
            current_user.save()
            login(request,current_user)
            return redirect(to = "perfil")
        else:
            return render(request,"gestion_de_usuarios/editar_perfil.html",data)
        
def eliminar_usuario(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_user.delete()
        return redirect(to = "home")


