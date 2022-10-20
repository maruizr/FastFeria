from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns=[ 
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('ventas/',ventasLocales, name="ventas"),
    path('usuarios/',agregarUsuarios, name="usuarios"),
    path('agregar-producto/', agregarProducto, name="agregar-producto"),
    path('productos/', listarProducto, name="productos"),
    path('agregar-pedido/', agregarPedido, name="agregar-pedido"),
    path('pedidos/', listarPedido, name="pedidos"),
]