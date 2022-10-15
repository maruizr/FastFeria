from django.shortcuts import render
from .models import VentLocal, VentExtran, Usuarios
from .forms import AgregarUsuForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    return render(request, 'registration/registro.html')

#Formato del Listar
def listarVentLocal(request):
    #Accediendo al objeto que contiene los datos en la base de datos
    #con el .all() se traen todos los objetos que esten en la tabla
    ventas = VentLocal.objects.all()
    # con esta variable 'ventas' se le pasa los datos al template
    datos = {
        'ventas': ventas
    }

    #ahora hay que retornar todo para que lo envie al template
    return render(request, 'ventas/listarVentaLocal.html', datos)

def agregarUsuarios(request):
    #crea la variable "form" para posteriormente llamarla en la plantilla html
    data = {
        # AgregarUsuForm() es una funcion creada en forms.py para generar formularios automaticamente
        # https://www.youtube.com/watch?v=90M4gunBRLs&list=PL3XiwX4b6ls0Ye0IkKgZpxzXh3EGe_TOJ&index=7
        # Dejo video tutorial usado para crearlo, Se recomienda seguir el hilo de estos videos
        # para que todo sea compatible.
        'form': AgregarUsuForm()
    }
    # verifica que los datos esten correctos y si tienen el metodo 'POST' para enviarlos a base de datos
    # Ademas crea la variable "mensaje" para informar en la plantilla que esta agregado
    if request.method == 'POST':
        formulario = AgregarUsuForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado"
        else:
            data["form"] = formulario
    return render(request, 'registration/agregarUsuarios.html', data )
