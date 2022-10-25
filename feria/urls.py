from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns=[ 
    path('index/', index, name="index"),
    path('registro/', registro, name="registro"),
    path('ventas/',ventasLocales, name="ventas"),
    path('agregar-producto/', agregarProducto, name="agregar-producto"),
    path('productos/', listarProducto, name="productos"),
    path('agregar-pedido/', agregarPedido, name="agregar-pedido"),
    path('pedidos/', listarPedido, name="pedidos"),
    path('MetodoPago/', agregarMetodoPago, name="agregarMetodoPago"),
    path('RecargarSaldo/', recargadeSaldo, name="recargadeSaldo"),
    path('ProcesoVenta/', procesodeVenta, name="procesodeVenta"),
    path('agregarprocesoventas/<int:id_proc_pedido>', agregarProcesoVenta, name="agregarProcesoVenta"),


]