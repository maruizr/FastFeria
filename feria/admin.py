from django.contrib import admin
from .models import Contratos ,DetallCompra, MetodoPago, Pedido, ProcesPedido, ProcesVenta, Productos, Recargas, ReportMerma,  ReportVenta, Reportes, Saldos, Seguimiento, Transporte, VentExtran, VentLocal
from usuario.models import Usuario
#Register your models here.
admin.site.register(Contratos)
admin.site.register(DetallCompra)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(ProcesPedido)
admin.site.register(ProcesVenta)
admin.site.register(Productos)
admin.site.register(Recargas)
admin.site.register(ReportMerma)
admin.site.register(ReportVenta)
admin.site.register(Reportes)
admin.site.register(Saldos)
admin.site.register(Seguimiento)
admin.site.register(Transporte)
admin.site.register(VentExtran)
admin.site.register(VentLocal)
