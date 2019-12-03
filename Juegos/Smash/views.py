#renderizar cualquier template que creemos
from django.shortcuts import render

#formas de autenticar y login de django
from django.contrib.auth import authenticate, login, logout

#redireccion a paginas mediante string
from django.http import HttpResponseRedirect, HttpResponse

#llamar urls usando el nombre de la url
from django.urls import reverse

#los forms que creamos en forms.py
from .forms import RegistrarForm, PerfilUsuarioForm, ImagenForm

from django.shortcuts import render
from .models import Image

#redireccion a index despues de hacer logout
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('Smash:index'))

#pagina principal
def index(request):
    return render(request, 'Smash/index.html', {})

#pagina de la galeria
def galeria(request):
    return render(request, 'Smash/galeria.html', {})

#pagina de contacto
def contacto(request):
    return render(request, 'Smash/contacto.html', {})

#pagina para subir imagenes
def subir(request):
    return render(request, 'Smash/subir.html', {})

#Login usuario
def login_usuario(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Smash:index'))
    else:
        if request.method == 'POST':
            #obtener campos desde el formulario y los asigno a las variables username y password
            username = request.POST.get('username')
            password = request.POST.get('password')
            #y lo autenticamos, si es que funciona devuelve el objeto y si no lo devuelve vacio
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Smash:index'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva")
            else:
                return HttpResponse("Datos invalidos")
        else:
            return render(request, 'Smash/login.html')

def registrar(request):
    registrado = False
    if request.method == 'POST':
        #Obtengo la informacion desde el formulario y la paso a las variables user_form y profile_form
        user_form = RegistrarForm(data=request.POST)
        profile_form = PerfilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #user_form.save lo guarda directamente en la base de datos
            user = user_form.save()
            #le asigna la password al usuario
            user.set_password(user.password)
            # y lo guarda
            user.save()
            # despues asigna imagen sin guardar aun
            profile = profile_form.save(commit=False)
            profile.user = user
            #Y si es que existe la imagen se le asigna al perfil
            if 'foto_perfil' in request.FILES:
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registrado = True
        else:
            return HttpResponse("Datos invalidos")
    else:
        user_form = RegistrarForm()
        profile_form = PerfilUsuarioForm()

    return render(request, 'Smash/registrar.html',
        {'user_form': user_form,
         'profile_form': profile_form,
         'registrado': registrado})

def subirImagen(request):
    if request.method == 'POST':
        imagen_form = ImagenForm(data=request.POST)
        if imagen_form.is_valid():
            if 'imagen' in request.FILES:
                image = imagen_form.save()
                image.imagen = request.FILES['imagen']
                image.save()
        else:
            return HttpResponse("Datos invalidos")
    else:
        image_form = RegistrarForm()
