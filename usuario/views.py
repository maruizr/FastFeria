from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import FormularioUsuario
from .models import Usuario
# Create your views here.

class ListadoUsuarios(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'
    queryset = Usuario.objects.filter(usuario_activo=True)


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('usuario:listado_usuarios')


def EditarUsuario(request, id):
    usuario = get_object_or_404(id=id)
    data = {
        'form': FormularioUsuario(instance=usuario)
    }
    return render(request, 'usuarios/editar_usuario.html')