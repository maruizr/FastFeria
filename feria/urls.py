from unicodedata import name
from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns=[ 
    path('index/', login_required(index), name="index"),
    path('registro/', login_required(registro), name="registro"),
    path('AgregarVentaLocal/',login_required(Agregar_ventas_Locales), name="AgregarVentaLol"),
    path('usuarios/',login_required(agregarUsuarios), name="usuarios"),
    path('agregar-producto/', login_required(agregarProducto), name="agregar-producto"),
    path('productos/', login_required(listarProducto), name="productos"),
    path('agregar-pedido/', login_required(agregarPedido), name="agregar-pedido"),
    path('pedidos/', login_required(listarPedido), name="pedidos"),
    path('MetodoPago/', login_required(agregarMetodoPago), name="agregarMetodoPago"),
    path('RecargarSaldo/', login_required(recargadeSaldo), name="recargadeSaldo"),
    path('ProcesoVenta/', login_required(procesodeVenta), name="procesodeVenta"),
    path('agregarprocesoventas/<int:id_proc_pedido>', login_required(agregarProcesoVenta), name="agregarProcesoVenta"),
    path('ventasLocales/', login_required(listarVentasLocales), name="Ventas Locales"),
    path('ingresar-transporte/', login_required(ingresar_transporte), name="ingresar-transporte"),
    path('listar-transporte/', login_required(listar_transporte), name="listar-transporte"),
    path('informe-externo/', login_required(informeexterno), name="informeexterno"),
    path('informe-interno/', login_required(informeinterno), name="informeinterno"),

]