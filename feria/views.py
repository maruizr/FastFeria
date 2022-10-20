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

def agregarUsuarios(request):
    data = {
        'usuarios': listar_usuarios()
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

def agregarProducto(request):
    data = {
        'usuarios': listar_usuarios(),
    }

    if request.method == 'POST':
        nom_prod = request.POST.get('nombre')
        precio_prod = request.POST.get('precio')
        desc_prod = request.POST.get('descripcion')
        stock_prod = request.POST.get('stock')
        usuarios_id = request.POST.get('usuarios')
        foto = request.FILES['foto'].read()

        salida = agregar_producto(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_id, foto)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            return redirect('listarProducto')
        else:
            data['mensaje'] = 'no se ha podido guardar'
        
    return render(request, 'productos/agregarProducto.html', data)

def agregarPedido(request):
    data = {
        'productos': listar_productos(),
        'usuarios': listar_usuarios(),
    }

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        cantidad = request.POST.get('cantidad') 
        fecha = request.POST.get('fecha')
        descrip = request.POST.get('descrip')
        usuarios_id = request.POST.get('usuarios')
        productos = request.POST.get('productos')
        estado_admin = request.POST.get('estado_admin')
        estado_productor = request.POST.get('estado_productor')
        refrigeracion = request.POST.get('refrigeracion')
        estado_edit_user = request.POST.get('estado_edit_user')
        estado_edit_admin = request.POST.get('estado_edit_admin')

        salida = agregar_pedido(tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido agregar'

    return render(request, 'pedido/agregarPedido.html', data)

def listarPedido(request):

    data = {
        'pedido': listar_pedido,
        'productos': listar_productos
    }

    return render(request, 'pedido/listarPedidos.html', data)

def listarProducto(request):

    data = {
        'productos': listar_productos
    }

    return render(request, 'productos/listarProductos.html', data)

def listar_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_USUARIOS', [out_cur])

    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
            'foto':str(base64.b64encode(fila[8].read()), 'utf-8')
        }
        lista.append(data)
        
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

def agregar_producto(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_id, foto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FASTFERIA.SP_AGREGAR_PRODUCTO', [nom_prod, precio_prod, desc_prod, stock_prod, usuarios_id, foto, salida])

    return salida.getvalue()

def listar_pedido():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FASTFERIA.SP_LISTAR_PEDIDO', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista

def agregar_pedido(tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FASTFERIA.SP_AGREGAR_PEDIDO', [tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin, salida])


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