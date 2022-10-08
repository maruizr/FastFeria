from django.urls import path 
from .views import index, login, listarVentLocal, registro

urlpatterns=[ 
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('ventas/',listarVentLocal, name="ventas")
]