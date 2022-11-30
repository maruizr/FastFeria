from unicodedata import name
from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns=[ 
    path('index/' ,login_required(index), name="index"),
    path('agregar-venta-local/',login_required(Agregar_ventas_Locales), name="agregar-venta-local"),
    path('agregar-producto/', login_required(agregarProducto), name="agregar-producto"),
    path('productos/', login_required(listarProducto), name="productos"),
    path('agregar-pedido/', login_required(agregarPedido), name="agregar-pedido"),
    path('pedidos/', login_required(listarPedido), name="pedidos"),
    path('metodo-pago/', login_required(agregarMetodoPago), name="agregar-metodo-pago"),
    path('pago/', login_required(pago), name="pago"),
    path('proceso-venta/', login_required(procesodeVenta), name="proceso-venta"),
    path('agregar-proceso-ventas/<int:id_proc_pedido>', login_required(agregarProcesoVenta), name="agregar-proceso-venta"),
    path('ventas-locales/', login_required(listarVentasLocales), name="ventas-locales"),
    path('ingresar-transporte/', login_required(ingresar_transporte), name="ingresar-transporte"),
    path('listar-transporte/', login_required(listar_transporte), name="listar-transporte"),
    path('informe-externo/', login_required(informeexterno), name="informe-externo"),
    path('informe-interno/', login_required(informeinterno), name="informe-interno"),
    path('proceso-pedido/<int:id>', login_required(ProcesoPedido), name="proceso-pedido"),
    path('listar-productores/', login_required(listadoproductores), name="listar-productores"),
    path('editar-productor/<int:id>/', login_required(Editarproductores), name="editar-productores"),
    path('registrar-productor/', login_required(RegistrarProductor.as_view()), name="registrar-productores"),
    path('eliminar-productor/<int:id>/', login_required(Eliminarproductor), name="eliminar-productores"),
    path('ver-productos/<int:id>/', login_required(Verproductos), name="ver-productos"),
    path('perfil-productor/', login_required(perfilproductor), name="perfil-productor"),
    path('listar-externos/', login_required(listadoexternos), name="lista-externos"),
    path('editar-externos/<int:id>/', login_required(Editarexternos), name="editar-externos"),
    path('eliminar-externos/<int:id>/', login_required(Eliminarexternos), name="eliminar-externos"),
    path('editar-venta-local/<int:id_vent_loc>/', login_required(EditarVentaLocal), name="editar-venta-local"),
    path('eliminar-venta-local/<int:id_vent_loc>/', login_required(EliminarVentaLocal), name="eliminar-venta-local"),
    path('compras/', login_required(compras), name="compras"),
    path('detalle-compra/<int:id>', login_required(detallecompra), name="detallecompra"),
    path('listado_usuarios/', login_required(ListadoUsuarios.as_view()),name='listado_usuarios'),
    path('registrar_usuarios/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario'),

]