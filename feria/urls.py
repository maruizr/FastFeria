from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns=[ 
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('ventas/',ventasLocales, name="ventas"),
    path('agregarUsuario/',agregarUsuarios, name="agregarUsuarios"),
    path('usuarios/',usuarios, name="usuarios"),
    path('agregar-producto/', agregarProducto, name="agregarProducto"),
    path('productos/', listarProducto, name="listarProducto"),
]