from multiprocessing import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
import cx_Oracle
import base64
from django.core.files.base import ContentFile
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    return render(request, 'registration/registro.html')

def ventasLocales(request):
    data = {
        'proceso_Venta': listar_procesoVenta(),
        'venta_Local': listar_ventaLocal(request)
    }

    if request.method == 'POST':
        proceso_venta = request.POST.get('procesosventas')
        nom_cli = request.POST.get('nombre_cliente')
        ape_cli = request.POST.get('apellido_cliente')
        email = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        num_calle = request.POST.get('num_calle')
        depto = request.POST.get('depto')
        region = request.POST.get('region')
        comuna = request.POST.get('comuna')
        salida = agregar_ventaLocal(proceso_venta, nom_cli, ape_cli, email, direccion, num_calle, depto, region, comuna)
        if salida == 1:
            data['mensaje'] = 'Se agrego la weaasdkfjhaskdjfhasdkjfh'
            return redirect('ventas')
        else:
            data['mensaje'] = 'no se agregojfh'


    return render(request, 'ventas/listarVentaLocal.html', data)

def listar_ventaLocal(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_VENTALOCAL', [out_cur])

    lista = []
    for i in out_cur:
        data = {
            'data': i,
            }
        lista.append(data)

    return lista

def listar_procesoVenta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_PROCESO_VENTA', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_ventaLocal(proces_venta, nom_cli, ape_cli, email, direc_cli, num_calle, depto, region, comuna):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FASTFERIA.SP_AGREGAR_VENTALOCAL', [proces_venta, nom_cli, ape_cli, email, direc_cli, num_calle, depto, region, comuna, salida])

    return salida.getvalue()

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
    return render(request, 'registration/agregarUsuarios.html', data)

def agregarProducto(request):
    data = {
        'usuarios': listar_usuarios(),
    }

    if request.method == 'POST':
        nom_prod = request.POST.get('nombre')
        precio_prod = request.POST.get('precio')
        desc_prod = request.POST.get('descripcion')
        stock_prod = request.POST.get('stock')
        usuarios_rut = request.POST.get('usuarios')
        foto = request.FILES['foto'].read()

        salida = agregar_producto(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_rut, foto)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            return redirect('listarProducto')
        else:
            data['mensaje'] = 'no se ha podido guardar'
        
    return render(request, 'productos/agregarProducto.html', data)

def listarProducto(request):

    data = {
        'productos': listar_productos
    }

    return render(request, 'productos/listarProductos.html', data)

def usuarios(request):

    datos_usuarios = listar_usuarios()

    arreglo = []
    for i in datos_usuarios:
        data = {
            'data': i,
            'foto':str(base64.b64encode(i[8].read()), 'utf-8')
        }
        arreglo.append(data)

    data = {
        'usuarios': arreglo,
    }

    if request.method== 'POST':
        rut_usr = request.POST.get('Rut')
        nombre = request.POST.get('Nombre')
        apellido_p = request.POST.get('ApellidoP')
        apellido_m = request.POST.get('ApellidoM')
        direccion = request.POST.get('Direccion')
        telefono = request.POST.get('Telefono')
        correo = request.POST.get('Correo')
        foto = request.FILES['foto'].read()
        contrasena = request.POST.get('Contraseña')
        rol = request.POST.get('Rol')
        
        salida = agregar_usuarios(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            return redirect('usuarios')
        else:
            data['mensaje'] = 'no se pudo agregar'

    return render(request, "usuarios/listarUsuarios.html", data)

def listar_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_USUARIOS', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
        

    return lista
    
    

def agregar_usuarios(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FASTFERIA.SP_AGREGAR_USUARIOS', [rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol, salida])

    return salida.getvalue()


def listar_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_PRODUCTOS', [out_cur])

    lista = []
    for i in out_cur:
        data = {
            'data': i,
            'imagen':str(base64.b64encode(i[6].read()), 'utf-8')
            }
        lista.append(data)

    return lista

def agregar_producto(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_rut, foto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FASTFERIA.SP_AGREGAR_PRODUCTO', [nom_prod, precio_prod, desc_prod, stock_prod, usuarios_rut, foto, salida])

    return salida.getvalue()
