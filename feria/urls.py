from unicodedata import name
from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns=[ 
    path('dashboard/', login_required(dashboard), name="dashboard"),
    path('dashboard/tables/<int:id>/', login_required(tables), name="tables"),
    path('index/' ,login_required(index), name="index"),
    path('registro/', login_required(registro), name="registro"),
    path('AgregarVentaLocal/',login_required(Agregar_ventas_Locales), name="AgregarVentaLol"),
    path('agregar-producto/', login_required(agregarProducto), name="agregar-producto"),
    path('productos/', login_required(listarProducto), name="productos"),
    path('agregar-pedido/', login_required(agregarPedido), name="agregar-pedido"),
    path('pedidos/', login_required(listarPedido), name="pedidos"),
    path('MetodoPago/', login_required(agregarMetodoPago), name="agregarMetodoPago"),
    path('RecargarSaldo/', login_required(recargadeSaldo), name="recargadeSaldo"),
    path('ProcesoVenta/', login_required(procesodeVenta), name="procesodeVenta"),
    path('agregarprocesoventas/<int:id_proc_pedido>', login_required(agregarProcesoVenta), name="agregarProcesoVenta"),
    path('ventasLocales/', login_required(listarVentasLocales), name="VentasLocales"),
    path('ingresar-transporte/', login_required(ingresar_transporte), name="ingresar-transporte"),
    path('listar-transporte/', login_required(listar_transporte), name="listar-transporte"),
    path('informe-externo/', login_required(informeexterno), name="informeexterno"),
    path('informe-interno/', login_required(informeinterno), name="informeinterno"),
    path('Proceso-Pedido/', login_required(ProcesoPedido), name="Proceso-Pedido"),
    path('publicarpedido/', login_required(publicarpedido), name="publicarpedido"),
    path('listar_productores/', login_required(listadoproductores), name="listar_productores"),
    path('editar_productor/<int:id>/', login_required(Editarproductores), name="editar_productores"),
    path('registrar_productor/', login_required(RegistrarProductor.as_view()), name="registrar_productores"),
    path('eliminar_productor/<int:id>/', login_required(Eliminarproductor), name="eliminar_productores"),
    path('ver_productos/<int:id>/', login_required(Verproductos), name="ver_productos"),
    path('listar_externos/', login_required(listadoexternos), name="listar_externos"),
    path('editar_externos/<int:id>/', login_required(Editarexternos), name="editar_externos"),
    path('eliminar_externos/<int:id>/', login_required(Eliminarexternos), name="eliminar_externos"),
    path('editar-ventaLocal/<int:id_vent_loc>/', login_required(EditarVentaLocal), name="editar_ventaLocal"),
    path('eliminar_ventaLocal/<int:id_vent_loc>/', login_required(EliminarVentaLocal), name="eliminar_ventaLocal"),

]