from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistrarUsuario, ListadoUsuarios, EditarUsuario, EliminarUsuario

urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuarios.as_view()),name='listado_usuarios'),
    path('registrar_usuarios/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario'),
    path('editar_usuarios/<int:id>/',login_required(EditarUsuario),name='editar_usuario'),
    path('eliminar_usuario/<int:id>/',login_required(EliminarUsuario),name='eliminar_usuario'),

    
]