from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns=[ 
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('ventas/',listarVentLocal, name="ventas"),
    path('agregarUsuario/',agregarUsuarios, name="agregarUsuarios"),
    path('productos/', agregarProducto, name="agregarProducto"),
    path('listarProd/', listarProducto, name="listarProducto"),
]