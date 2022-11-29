from unicodedata import name
from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns=[ 
    path('dashboard/tables/<int:id>/', login_required(tables), name="tables"),
    path('index/' ,login_required(index), name="index"),
    path('registro/', login_required(registro), name="registro"),
    path('agregar-venta-local/',login_required(Agregar_ventas_Locales), name="agregar-venta-local"),
    path('agregar-producto/', login_required(agregarProducto), name="agregar-producto"),
    path('productos/', login_required(listarProducto), name="productos"),
    path('agregar-pedido/', login_required(agregarPedido), name="agregar-pedido"),
    path('pedidos/', login_required(listarPedido), name="pedidos"),
    path('metodo-pago/', login_required(agregarMetodoPago), name="agregar-metodo-pago"),
    path('recargar-saldo/', login_required(recargadeSaldo), name="recarga-saldo"),
    path('proceso-venta/', login_required(procesodeVenta), name="proceso-venta"),
    path('agregar-proceso-ventas/<int:id_proc_pedido>', login_required(agregarProcesoVenta), name="agregar-proceso-venta"),
    path('ventas-locales/', login_required(listarVentasLocales), name="ventas-locales"),
    path('ingresar-transporte/', login_required(ingresar_transporte), name="ingresar-transporte"),
    path('listar-transporte/', login_required(listar_transporte), name="listar-transporte"),
    path('informe-externo/', login_required(informeexterno), name="informe-externo"),
    path('informe-interno/', login_required(informeinterno), name="informe-interno"),
    path('proceso-pedido/<int:id>', login_required(ProcesoPedido), name="proceso-pedido"),
    path('publicar-pedido/', login_required(publicarpedido), name="publicar-pedido"),
    path('listar-productor/', login_required(listadoproductores), name="listar-productores"),
    path('editar-productor/<int:id>/', login_required(Editarproductores), name="editar-productores"),
    path('registrar-productor/', login_required(RegistrarProductor.as_view()), name="registrar-productores"),
    path('eliminar-productor/<int:id>/', login_required(Eliminarproductor), name="eliminar-productores"),
    path('ver-productos/<int:id>/', login_required(Verproductos), name="ver-productos"),
    path('listar-externos/', login_required(listadoexternos), name="lista-externos"),
    path('editar-externos/<int:id>/', login_required(Editarexternos), name="editar-externos"),
    path('eliminar-externos/<int:id>/', login_required(Eliminarexternos), name="eliminar-externos"),
    path('editar-venta-local/<int:id_vent_loc>/', login_required(EditarVentaLocal), name="editar-venta-local"),
    path('eliminar-venta-local/<int:id_vent_loc>/', login_required(EliminarVentaLocal), name="eliminar-venta-local"),

]