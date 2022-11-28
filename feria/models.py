# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Contratos(models.Model):
    id_contrat = models.AutoField(primary_key=True)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    emision_contrat = models.DateField()
    fin_contrat = models.DateField()
    estado = models.BooleanField()
    foto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos'


class DetallCompra(models.Model):
    id_detall = models.AutoField(primary_key=True)
    proces_venta = models.ForeignKey('ProcesVenta', models.DO_NOTHING, db_column='proces_venta')
    fecha_detall = models.DateField()
    nom_producto = models.CharField(max_length=15)
    cost_producto = models.IntegerField()
    cantidad = models.IntegerField()
    iva_producto = models.IntegerField()
    total_compra = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detall_compra'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MetodoPago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    tipo_cuenta = models.CharField(max_length=20)
    numero_cuenta = models.BigIntegerField()
    tipo_banco = models.CharField(max_length=20)
    nombre_titular = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    descrip = models.CharField(max_length=200)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    productos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos', blank=True, null=True)
    estado_admin = models.BooleanField()
    estado_productor = models.BooleanField()
    refrigeracion = models.BooleanField()
    estado_edit_user = models.BooleanField()
    estado_edit_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pedido'


class ProcesPedido(models.Model):
    id_proc_pedido = models.AutoField(primary_key=True)
    transportes = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='transportes')
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido')
    estado_proceso = models.BooleanField()
    estado_seguimiento = models.BooleanField()
    estado_proces_venta = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'proces_pedido'


class ProcesVenta(models.Model):
    id_proc_venta = models.AutoField(primary_key=True)
    proces_pedido = models.ForeignKey(ProcesPedido, models.DO_NOTHING, db_column='proces_pedido')
    estado_pago_cliente = models.BooleanField()
    estado_pago_product = models.BooleanField()
    estado_pago_transport = models.BooleanField()
    estado_venta = models.BooleanField()
    estado_detalle = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'proces_venta'


class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=20)
    precio_prod = models.IntegerField()
    desc_prod = models.CharField(max_length=200)
    stock_prod = models.IntegerField()
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    foto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Recargas(models.Model):
    id_recarga = models.AutoField(primary_key=True)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='metodo_pago')
    saldo_recargado = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'recargas'


class ReportMerma(models.Model):
    id_merma = models.AutoField(primary_key=True)
    fecha_merma = models.DateField()
    descrip_merma = models.CharField(max_length=40)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_merma'


class ReportVenta(models.Model):
    id_report_vent = models.AutoField(primary_key=True)
    prod_venta = models.CharField(max_length=20)
    cant_venta = models.IntegerField()
    total_venta = models.IntegerField()
    proces_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta')

    class Meta:
        managed = False
        db_table = 'report_venta'


class Reportes(models.Model):
    id_report = models.AutoField(primary_key=True)
    fecha_report = models.DateField()
    tip_report = models.CharField(max_length=15)
    user_report = models.CharField(max_length=15)
    descrip_report = models.CharField(max_length=30)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reportes'


class Saldos(models.Model):
    id_saldo = models.AutoField(primary_key=True)
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    recargas = models.ForeignKey(Recargas, models.DO_NOTHING, db_column='recargas', blank=True, null=True)
    saldo_total = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saldos'


class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    est_seguimiento = models.CharField(max_length=20)
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido')
    proces_pedido = models.ForeignKey(ProcesPedido, models.DO_NOTHING, db_column='proces_pedido')

    class Meta:
        managed = False
        db_table = 'seguimiento'


class Transporte(models.Model):
    id_trans = models.AutoField(primary_key=True)
    tip_transporte = models.CharField(max_length=15)
    tamano_trans = models.IntegerField()
    capacidad_trans = models.IntegerField()
    refrigeracion_trans = models.BooleanField()
    usuarios = models.ForeignKey('UsuarioUsuario', models.DO_NOTHING)
    foto = models.BinaryField(blank=True, null=True)
    patente = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'transporte'


class UsuarioUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    nombres = models.CharField(max_length=200, blank=True, null=True)
    apellidos = models.CharField(max_length=200, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(blank=True, null=True)
    usuario_administrador = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    tipo_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_usuario'


class VentExtran(models.Model):
    id_vent_ex = models.AutoField(primary_key=True)
    proces_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta')
    nom_cli = models.CharField(max_length=30)
    ape_cli = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    direc_cli = models.CharField(max_length=50)
    num_calle = models.IntegerField()
    depto = models.IntegerField()
    localidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vent_extran'


class VentLocal(models.Model):
    id_vent_loc = models.AutoField(primary_key=True)
    proces_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta')
    nom_cli = models.CharField(max_length=30)
    ape_cli = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    direc_cli = models.CharField(max_length=50)
    num_calle = models.IntegerField()
    depto = models.IntegerField()
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vent_local'
