from django.urls import path 
from .views import index, login, listarVentLocal, registro, agregarUsuarios

urlpatterns=[ 
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('ventas/',listarVentLocal, name="ventas"),
    path('agregarUsuario/',agregarUsuarios, name="agregarUsuarios")
]