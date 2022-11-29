from multiprocessing import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db import connection
import cx_Oracle
import base64
from django.core.files.base import ContentFile
from .models import *
from .forms import *
from FastFeria import settings
from django.urls import reverse_lazy
from usuario.models import Usuario
from usuario.forms import FormularioUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.mail import send_mail


# Create your views here.

def index(request):
    # user = Usuario.objects.all()
    # data = {
    #     'user' : user

    # }
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    return render(request, 'registration/registro.html')

def dashboard(request):
    return render(request, 'dashboard/index.html')

def tables(request,id):
    usuario = get_object_or_404(Usuario, id=id)
    users = Usuario.objects.all()
    data = {
        'form': FormularioUsuario(instance=usuario),
        'users' : users
    }
    if request.method == 'POST':
        formulario = FormularioUsuario(data = request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_externos")
        data["form"] = formulario
    return render(request, 'dashboard/pages/tables.html', data)

def Agregar_ventas_Locales(request):
    data = {
        'proceso_Venta': listar_procesoVenta(),
        # 'region': listregiones(),
        # 'comuna': listcomunas()
        

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
            subject = "Agregado"
            message = "Has agregado una venta local"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'feriafastoficial@gmail.com']
            recipient_list = ["feriafastoficial@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje'] = 'Se agregó la venta local'
            return redirect('VentasLocales')
        else:
            data['mensaje'] = 'no se agregó'


    return render(request, 'ventas/AgregarVentaLocal.html', data)

def listarVentasLocales(request):
    venta_Local = VentLocal.objects.all()
    data = {
        'venta_Local': venta_Local
    }

    return render(request, 'ventas/ListarVentaLocal.html', data)

def agregarProducto(request):
    # data = {
    #     'usuarios': listar_usuarios(),
    # }
    # user = Usuario.objects.all()
    # data = {
    #      'user': user,
    # }
    data = {
        'mensaje1': "agregado correctamente",
        'mensaje2': "no se ha podido guardar"
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
            subject = "Agregado"
            message = "Has agregado un producto"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'fastferia3@gmail.com']
            recipient_list = ["fastferia3@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje1'] 
            return redirect('productos')
        else:
            data['mensaje2']
        
    return render(request, 'productos/agregarProducto.html', data)

def agregarPedido(request):
    data = {
        'productos': listar_productos(),
        'usuarios': Usuario.objects.all(),
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
            subject = "Agregado"
            message = "Has agregado un pedido"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'feriafastoficial@gmail.com']
            recipient_list = ["feriafastoficial@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido agregar'

    return render(request, 'pedido/agregarPedido.html', data)

def publicarpedido(request):
    data = {
        'pedido': listar_pedido,
        'productos': listar_productos
    }

    return render(request, 'dashboard/pages/publicarproceso.html', data)   

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

# def listar_usuarios():
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc('FERIAFAST.SP_LISTAR_USUARIOS', [out_cur])

#     lista = []
#     for fila in out_cur:
#         data = {
#             'data': fila,
#             'foto':str(base64.b64encode(fila[8].read()), 'utf-8')
#         }
#         lista.append(data)
        
#     return lista

# def agregar_usuarios(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     salida = cursor.var(cx_Oracle.NUMBER)
#     cursor.callproc('FERIAFAST.SP_AGREGAR_USUARIOS', [rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol, salida])

#     return salida.getvalue()


def listar_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_PRODUCTOS', [out_cur])

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
    cursor.callproc('FERIAFAST.SP_AGREGAR_PRODUCTO', [nom_prod, precio_prod, desc_prod, stock_prod, usuarios_id, foto, salida])

    return salida.getvalue()

def agregar_pedido(tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_AGREGAR_PEDIDO', [tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin, salida])


def listar_ventaLocal(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_VENTALOCAL', [out_cur])

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

    cursor.callproc('FERIAFAST.SP_LISTAR_PROCESO_VENTA', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_ventaLocal(proces_venta, nom_cli, ape_cli, email, direc_cli, num_calle, depto, region, comuna):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_AGREGAR_VENTALOCAL', [proces_venta, nom_cli, ape_cli, email, direc_cli, num_calle, depto, region, comuna, salida])

    return salida.getvalue()

def informeexterno(request):

    data = {
        'proces_pedido': listar_proces_pedido(),
        'pedido': listar_pedido(),
        'listaprocesventa': DetallCompra.objects.all(),
        'ventextran': VentExtran.objects.all(),
        'tran': Transporte.objects.all(),
        'ped': Pedido.objects.all(),
        
        
    }  
    return render(request, 'ventas/informeventaexterna.html', data)
   
def informeinterno(request):

    data = {
        'proces_pedido': listar_proces_pedido(),
        'pedido': listar_pedido(),
        'listaprocesventa': DetallCompra.objects.all(),
        'ventlocal': VentLocal.objects.all(),
        'tran': Transporte.objects.all(),
        'ped': Pedido.objects.all(),
       
        
    }  
    return render(request, 'ventas/informeventalocal.html', data)

def agregarMetodoPago(request):
    data = {
        'mensaje1': "agregado correctamente",
        'mensaje2': "no se ha podido guardar"
    }

    if request.method == 'POST':
        usuarios_id = request.POST.get('usuarios')
        tipo_cuenta = request.POST.get('tipocuenta')
        numero_cuenta = request.POST.get('numerocuenta')
        tipo_banco = request.POST.get('tipobanco')
        nombre_titular = request.POST.get('nombretitular')
        #--
        recargas = ""
        saldo_total = "0"
        


        salida = agregar_metodopagos(usuarios_id, tipo_cuenta, numero_cuenta, tipo_banco, nombre_titular)
        salida = agregar_saldo(usuarios_id, recargas, saldo_total)
        
        if salida == 1:
            data['mensaje1'] 
            return redirect('agregarMetodoPago')
        else:
            data['mensaje2'] 
        
    return render(request, 'pagos/agregarMetodoPago.html', data)

def agregar_metodopagos(usuarios_id, tipo_cuenta, numero_cuenta, tipo_banco, nombre_titular):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_agregar_MetodoPago', [usuarios_id, tipo_cuenta, numero_cuenta, tipo_banco, nombre_titular, salida])

    return salida.getvalue()


def agregar_saldo(usuarios_id, recargas, saldo_total):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_comprar_saldos', [usuarios_id, recargas, saldo_total, salida])

    return salida.getvalue()

def recargadeSaldo(request):
    data = {
        'mensaje1': "agregado correctamente",
        'mensaje2': "no se ha podido guardar",
        'metodopagos': listar_metodopago(),
    }


    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        saldo_recargado = request.POST.get('saldorecargado')
       
        
        salida = recargar_saldo(metodo_pago, saldo_recargado)
        if salida == 1:
            subject = "Recargado"
            message = "Has agregado recargado saldo"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'fastferia3@gmail.com']
            recipient_list = ["fastferia3@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje1'] 
            return redirect('recargadeSaldo')
        else:
            data['mensaje2'] 
        
    return render(request, 'pagos/recargarSaldo.html', data)



def recargar_saldo(metodo_pago, saldo_recargado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_recargar_saldo', [metodo_pago, saldo_recargado, salida])

    return salida.getvalue()

def listar_metodopago():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_METODOPAGO', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista


def procesodeVenta(request):
    data = {
        'usuario': Usuario.objects.all(),
        'proces_pedido': listar_proces_pedido(),
        'pedido': listar_pedido(),
        'listprocespedido': ProcesPedido.objects.all(),
        'tran': Transporte.objects.all(),
        'ped': Pedido.objects.all(),
        'segui': Seguimiento.objects.all(),
        'productos': listar_productos(),
        
        
    }  
    est_seguimiento_condicion = request.POST.get('estadoseguimiento')
    if est_seguimiento_condicion == "Preparando Pedido":
            est_seguimiento = request.POST.get('estadoseguimiento')
            pedido = request.POST.get('numeropedido')
            proces_pedido = request.POST.get('numeroprocespedido')
            id_proc_pedido = request.POST.get('numeroprocespedido')
            salida = modificarseguimiento(id_proc_pedido)
            salida = agregar_seguimiento(est_seguimiento, pedido, proces_pedido)
            if salida == 1:
                data['mensaje'] = 'agregado correctamente'
            
            else:
                data['mensaje'] = 'no se ha podido guardar'
            
    if est_seguimiento_condicion == "En ruta":
            est_seguimiento = request.POST.get('estadoseguimiento')
            id_seguimiento = request.POST.get('idseguimiento')
            salida = modificarseguimientoestado(id_seguimiento, est_seguimiento)
            if salida == 1:
                data['mensaje'] = 'agregado correctamente'
            
            else:
                 data['mensaje'] = 'no se ha podido guardar'

    if est_seguimiento_condicion == "Entregado":
        est_seguimiento = request.POST.get('estadoseguimiento')
        id_seguimiento = request.POST.get('idseguimiento')
        salida = modificarseguimientoestado(id_seguimiento, est_seguimiento)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            
        else:
                data['mensaje'] = 'no se ha podido guardar'
    
    if est_seguimiento_condicion == "Finalizado":
        est_seguimiento = request.POST.get('estadoseguimiento')
        id_seguimiento = request.POST.get('idseguimiento')
        salida = modificarseguimientoestado(id_seguimiento, est_seguimiento)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            
        else:
                data['mensaje'] = 'no se ha podido guardar'
    return render(request, 'ventas/procesoVenta.html', data)


     
def modificarseguimiento(id_proc_pedido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_ProcesoPedidoUpdateSeguimientos', [id_proc_pedido, salida])

def modificarseguimientoestado(id_seguimiento, est_seguimiento):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_SEGUIMIENTOESTADODEPEDIDO', [id_seguimiento, est_seguimiento, salida])





def listar_proces_pedido():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_PROCES_VENTA', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_pedido():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_PEDIDO', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
        

    return lista

def agregarProcesoVenta(request,id_proc_pedido):
    data = {
        
        'idventa': ProcesPedido.objects.get(id_proc_pedido = id_proc_pedido),
        'ped': Pedido.objects.all(),
    }
    
    if request.method == 'POST':
        proces_pedido = id_proc_pedido
        id_proc_pedido = id_proc_pedido
        estado_pago_cliente = request.POST.get('numerocero')
        estado_pago_product = request.POST.get('numerocero')
        estado_pago_transport = request.POST.get('numerocero')
        estado_venta = request.POST.get('numerocero')
        estado_detalle = request.POST.get('numerocero')
       
        id_proc_pedido = request.POST.get('id_proc_pedido2')
        transportes = request.POST.get('transportes2')
        pedido = request.POST.get('pedido2')
        estado_proceso = request.POST.get('estado_proceso2')
        estado_proces_venta = request.POST.get('estado_proces_venta2')
        estado_seguimiento = request.POST.get('estado_seguimiento2')
        

        salida = agregar_procesoventa(proces_pedido, estado_pago_cliente, estado_pago_product, estado_pago_transport, estado_venta, estado_detalle)
        salida = modificarprimer(id_proc_pedido)
        
        if salida == 1:
            subject = "Agregado"
            message = "Has agregado un proceso de venta"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'feriafastoficial@gmail.com']
            recipient_list = ["feriafastoficial@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje'] = 'agregado correctamente'
            return redirect('procesodeVenta')
        else:
            data['mensaje'] = 'no se ha podido guardar'
        
    return render(request, 'ventas/agregarProcesoVenta.html', data)



def agregar_procesoventa(proces_pedido, estado_pago_cliente, estado_pago_product, estado_pago_transport, estado_venta, estado_detalle):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_agregar_ProcesVenta', [proces_pedido, estado_pago_cliente, estado_pago_product, estado_pago_transport, estado_venta, estado_detalle, salida])

    return salida.getvalue()

def modificarprimer(id_proc_pedido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_ProcesoPedidoUpdateEstados', [id_proc_pedido, salida])

    return salida.getvalue()



def editar_procesopedido(id_proc_pedido,estado_seguimiento):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida2 = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_UPDATE_ProcesPedidos', [id_proc_pedido,estado_seguimiento, salida2])

    return salida2.getvalue()



def ingresar_transporte(request):
    data = {
        'mensaje1': "agregado correctamente",
        'mensaje2': "no se ha podido guardar"
    }

    if request.method == 'POST':
        tip_transporte = request.POST.get('tipot')
        tamano_trans = request.POST.get('tamano')
        capacidad_trans = request.POST.get('capacidad')
        refri = request.POST.get('refri')
        if refri == "true":
            subject = "Ingresado"
            message = "Has ingresado un nuevo transporte"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'fastferia3@gmail.com']
            recipient_list = ["fastferia3@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje1'] 
            refrigeracion_trans = 1
        else:
            data['mensaje1'] 
            refrigeracion_trans = 0
        
        usuarios_id = request.POST.get('usuarios')
        foto = request.FILES['foto'].read()
        patente = request.POST.get('patente')

        salida = agregar_transporte(tip_transporte, tamano_trans, capacidad_trans, refrigeracion_trans, usuarios_id, foto, patente)
        if salida == 1:
            data['mensaje1'] 
            
        else:
            data['mensaje2']
        
    return render(request, 'transporte/ingresar-transporte.html', data)




def agregar_transporte(tip_transporte, tamano_trans, capacidad_trans, refrigeracion_trans, usuarios_id, foto, patente):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_AGREGAR_TRANSPORTE', [tip_transporte, tamano_trans, capacidad_trans, refrigeracion_trans, usuarios_id, foto, patente, salida])

    return salida.getvalue()




def listar_transporte(request):
    data2 = {
        'transporte': listartrans(),
    }


    return render(request, 'transporte/listarTransporte.html', data2)


def listartrans():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_TRANSPORTE', [out_cur])

    lista = []
    for i in out_cur:
        data = {
            'data': i,
            'imagen':str(base64.b64encode(i[6].read()), 'utf-8')
            }
        lista.append(data)

    return lista

def listregiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_REGION', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista

def listcomunas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('FERIAFAST.SP_LISTAR_COMUNA', [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista
    
def ProcesoPedido(request, id):
    data = {
        'usuarios': Usuario.objects.all(),
        'transporte': listartrans(),
        'transporte2': Transporte.objects.get(id_trans = id),
        'ped': Pedido.objects.all(),
    }

    if request.method == 'POST':
        transportes = request.POST.get('iddetransporte')
        pedido = request.POST.get('numeropedido')
        estado_proceso = request.POST.get('numerocero')
        estado_seguimiento = request.POST.get('numerocero')
        estado_proces_venta = request.POST.get('numerocero')




        
        

        salida = agregar_proces_pedido(transportes, pedido, estado_proceso, estado_seguimiento, estado_proces_venta)
        
        
        
        if salida == 1:
            subject = "Agregado"
            message = "Agregado correctamente"
            email_from = settings.EMAIL_HOST_USER
            to_email =  [Usuario.email, 'feriafastoficial@gmail.com']
            recipient_list = ["feriafastoficial@gmail.com"]
            send_mail(subject, message, email_from, to_email, recipient_list)
            data['mensaje'] = 'agregado correctamente'
            
        else:
            data['mensaje'] = 'no se ha podido guardar'
        
    return render(request, 'pedido/proces_pedido.html', data)

def agregar_proces_pedido(transportes, pedido, estado_proceso, estado_seguimiento, estado_proces_venta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_PROCESO_PEDIDO', [transportes, pedido, estado_proceso, estado_seguimiento, estado_proces_venta, salida])

    return salida.getvalue()

def agregar_seguimiento(est_seguimiento, pedido, proces_pedido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('FERIAFAST.SP_AGREGAR_Seguimiento', [est_seguimiento, pedido, proces_pedido, salida])

    return salida.getvalue()

def listadoproductores(request):
    productores = Usuario.objects.all()
    
    data = {
        'productores': productores,
    }
    return render(request, 'productores/listar_productores.html',data)

def Editarproductores(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': FormularioUsuario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = FormularioUsuario(data = request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productores")
        data["form"] = formulario
    return render(request, 'productores/editar_productor.html',data)

class RegistrarProductor(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'productores/registrar_productor.html'
    success_url = reverse_lazy('listar_productores')

def Eliminarproductor(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect(to="listar_productores")

def Verproductos(request,id):
    productores = get_object_or_404(Usuario, id=id)
    productos = Productos.objects.all()
    data={
        'productores': productores,
        'productos' : listar_productos(),
        'check': productos
    }
    return render(request, 'productores/ver_productos.html',data)

def listadoexternos(request):
    externos = Usuario.objects.all()
    
    data = {
        'externos': externos,
    }
    return render(request, 'externos/listar_externos.html',data)

def Editarexternos(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': FormularioUsuario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = FormularioUsuario(data = request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_externos")
        data["form"] = formulario
    return render(request, 'externos/editar_externos.html',data)

def Eliminarexternos(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect(to="listar_externos")


def EditarVentaLocal(request, id_vent_loc):
    venta = get_object_or_404(VentLocal, id_vent_loc=id_vent_loc)
    data = {
        'form': FormularioVentaLocal(instance=venta)
    }
    if request.method == 'POST':
        formulario = FormularioVentaLocal(data= request.POST, instance = venta, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="VentasLocales")
        data["form"] = formulario
    return render (request, 'ventas/EditarVentaLocal.html', data)

def EliminarVentaLocal(request, id_vent_loc):
    venta = get_object_or_404(VentLocal, id_vent_loc=id_vent_loc)
    venta.delete()
    return redirect(to="VentasLocales")

def detallecompra(request):
    
    return render(request, 'ventas/detallecompra.html')