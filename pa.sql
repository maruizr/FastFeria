CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_USUARIOS (usuarios out SYS_REFCURSOR)
IS 
BEGIN
    OPEN usuarios FOR SELECT * FROM usuarios;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_PRODUCTOS (productos out SYS_REFCURSOR)
IS 
BEGIN
    OPEN productos FOR SELECT * FROM productos;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_PEDIDO (pedido out SYS_REFCURSOR)
IS 
BEGIN
    OPEN pedido FOR SELECT * FROM pedido;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_REGION (region out SYS_REFCURSOR)
IS 
BEGIN
    OPEN region FOR SELECT * FROM region;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_COMUNA (comuna out SYS_REFCURSOR)
IS 
BEGIN
    OPEN comuna FOR SELECT * FROM comuna;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_AGREGAR_PRODUCTO(
    v_nom_prod VARCHAR2,
    v_precio_prod NUMBER,
    v_desc_prod VARCHAR2,
    v_stock_prod NUMBER,
    v_usuarios_id NUMBER,
    v_blob BLOB,
    v_salida OUT NUMBER
)
IS 
BEGIN
    INSERT INTO productos(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_id, foto)
    VALUES(v_nom_prod, v_precio_prod, v_desc_prod, v_stock_prod, v_usuarios_id, v_blob);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_AGREGAR_USUARIOS (
    v_rut_usr VARCHAR2,
    v_nombre VARCHAR2,
    v_apellido_p VARCHAR2,
    v_apellido_m VARCHAR2,
    v_direccion VARCHAR2,
    v_telefono NUMBER,
    v_correo VARCHAR2,
    v_blob BLOB, 
    v_contrasena VARCHAR2,
    v_rol number,
    v_salida out number
)
IS 
BEGIN
    INSERT INTO usuarios(rut_usr, nombre, apellido_p, apellido_m, direccion, telefono, correo, foto, contrasena, rol )
    VALUES(v_rut_usr, v_nombre, v_apellido_p, v_apellido_m, v_direccion, v_telefono, v_correo, v_blob, v_contrasena, v_rol);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    when OTHERS THEN
        v_salida:=0;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_AGREGAR_PEDIDO(
    v_tipo VARCHAR2,
    v_cantidad NUMBER,
    v_fecha DATE,
    v_descrip VARCHAR2,
    v_usuarios_id NUMBER,
    v_productos NUMBER,
    v_estado_admin NUMBER,
    v_estado_prod NUMBER,
    v_refrigeracion NUMBER,
    v_est_edit_user NUMBER,
    v_est_edit_admin NUMBER,
    v_salida OUT NUMBER
)
IS 
BEGIN
    INSERT INTO pedido(tipo, cantidad, fecha, descrip, usuarios_id, productos, estado_admin, estado_productor, refrigeracion, estado_edit_user, estado_edit_admin)
    VALUES(v_tipo, v_cantidad, v_fecha, v_descrip, v_usuarios_id, v_productos, v_estado_admin, v_estado_prod, v_refrigeracion, v_est_edit_user, v_est_edit_admin);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;


--


CREATE OR REPLACE PROCEDURE FERIAFAST.SP_agregar_MetodoPago(
    v_usuarios_id NUMBER,
    v_tipo_cuenta VARCHAR2,
    v_numero_cuenta NUMBER,
    v_tipo_banco VARCHAR2,
    v_nombre_titular VARCHAR2,
    v_salida OUT number
)
IS 
BEGIN
    INSERT INTO metodo_pago(usuarios_id, tipo_cuenta, numero_cuenta, tipo_banco, nombre_titular)
    VALUES(v_usuarios_id, v_tipo_cuenta, v_numero_cuenta, v_tipo_banco, v_nombre_titular);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;



CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_METODOPAGO (metodo_pago out SYS_REFCURSOR)
IS 
BEGIN
    OPEN metodo_pago FOR SELECT * FROM metodo_pago;
END;






CREATE OR REPLACE PROCEDURE FERIAFAST.SP_comprar_saldos(
    v_usuarios_id NUMBER,
    v_recargas NUMBER,
    v_saldo_total NUMBER,
    v_salida OUT number
)
IS 
BEGIN
    INSERT INTO saldos(usuarios_id, recargas, saldo_total)
    VALUES(v_usuarios_id, v_recargas, v_saldo_total);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;



CREATE OR REPLACE PROCEDURE FERIAFAST.SP_comprar_saldos(
    v_usuarios_id NUMBER,
    v_recargas NUMBER,
    v_saldo_total NUMBER,
    v_salida OUT number
)
IS 
BEGIN
    INSERT INTO saldos(usuarios_id, recargas, saldo_total)
    VALUES(v_usuarios_id, v_recargas, v_saldo_total);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_recargar_saldo(
    v_metodo_pago NUMBER,
    v_saldo_recargado NUMBER,
    v_salida OUT number
)
IS 
BEGIN
    INSERT INTO recargas(metodo_pago, saldo_recargado)
    VALUES(v_metodo_pago, v_saldo_recargado);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;


CREATE OR REPLACE PROCEDURE FERIAFAST.SP_agregar_ProcesVenta(
    v_proces_pedido NUMBER,
    v_estado_pago_cliente NUMBER,
    v_estado_pago_product NUMBER,
    v_estado_pago_transport NUMBER,
    v_estado_venta NUMBER,
    v_estado_detalle NUMBER,
    v_salida OUT number
)
IS 
BEGIN
    INSERT INTO proces_venta(proces_pedido, estado_pago_cliente, estado_pago_product, estado_pago_transport, estado_venta, estado_detalle)
    VALUES(v_proces_pedido, v_estado_pago_cliente, v_estado_pago_product, v_estado_pago_transport, v_estado_venta, v_estado_detalle);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_PROCES_VENTA (proces_venta out SYS_REFCURSOR)
IS 
BEGIN
    OPEN proces_venta FOR SELECT * FROM proces_venta;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_PROCES_PEDIDO (proces_pedido out SYS_REFCURSOR)
IS 
BEGIN
    OPEN proces_pedido FOR SELECT * FROM proces_pedido;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_PEDIDO (pedido out SYS_REFCURSOR)
IS 
BEGIN
    OPEN pedido FOR SELECT * FROM pedido;
END;



CREATE OR REPLACE PROCEDURE FERIAFAST.SP_AGREGAR_TRANSPORTE(
    v_tip_transporte NUMBER,
    v_tamano_trans VARCHAR2,
    v_capacidad_trans NUMBER,
    v_refrigeracion_trans NUMBER,
    v_usuarios_id NUMBER,
    v_blob BLOB,
	v_patente varchar2,
    v_salida OUT NUMBER
)
IS 
BEGIN
    INSERT INTO transporte(tip_transporte, tamano_trans, capacidad_trans, refrigeracion_trans, usuarios_id, foto, patente)
    VALUES(v_tip_transporte, v_tamano_trans, v_capacidad_trans, v_refrigeracion_trans, v_usuarios_id, v_blob, v_patente);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_LISTAR_TRANSPORTE (transporte out SYS_REFCURSOR)
IS 
BEGIN
    OPEN transporte FOR SELECT * FROM transporte;
END;

CREATE OR REPLACE PROCEDURE FERIAFAST.SP_ELIMINAR_PRODUCTO (id_prod NUMBER)
AS 
BEGIN
    UPDATE ejemplar 
    set estado = 'disponible' 
    WHERE id_ejem IN (  SELECT e.id_ejem FROM ejemplar E
                        INNER JOIN detalle_solicitud_prestamo DSP
                        ON (e.id_ejem = dsp.id_ejem)
                        WHERE numero_solicitud IN (   select dsp.numero_solicitud from detalle_solicitud_prestamo dsp
                        inner join prestamo p
                        on (dsp.numero_solicitud = p.numero_solicitud)
                        where p.rut_usr = v_rut_usr));
        
    DELETE FROM detalle_solicitud_prestamo
    WHERE numero_solicitud IN (   select dsp.numero_solicitud from detalle_solicitud_prestamo dsp
                    inner join prestamo p
                    on (dsp.numero_solicitud = p.numero_solicitud)
                    where p.rut_usr = v_rut_usr);

    DELETE FROM prestamo
    WHERE rut_usr = v_rut_usr;
        
    DELETE FROM solicitud_prestamo 
    WHERE usuario_rut_usr = v_rut_usr;
        
    DELETE FROM usuario
    WHERE rut_usr = v_rut_usr;
    COMMIT;
END SP_USUARIO_DELETE;


CREATE OR REPLACE PROCEDURE FERIAFAST.SP_ProcesoPedidoUpdateEstados (v_id_proc_pedido NUMBER, v_salida OUT NUMBER)


    AS 
    BEGIN
        UPDATE proces_pedido
        SET     estado_proces_venta = 1
            WHERE id_proc_pedido = v_id_proc_pedido;
        COMMIT;
		v_salida:=1;
	EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;

    END SP_ProcesoPedidoUpdateEstados;
	


	
CREATE OR REPLACE PROCEDURE FERIAFAST.SP_AGREGAR_Seguimiento (
    v_est_seguimiento VARCHAR2,
    v_pedido number,
    v_proces_pedido number,
    v_salida out number
)
IS 
BEGIN
    INSERT INTO seguimiento(est_seguimiento, pedido, proces_pedido )
    VALUES(v_est_seguimiento, v_pedido, v_proces_pedido);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    when OTHERS THEN
        v_salida:=0;
END;


CREATE OR REPLACE PROCEDURE FERIAFAST.SP_ProcesoPedidoUpdateSeguimientos (v_id_proc_pedido NUMBER, v_salida OUT NUMBER)


    AS 
    BEGIN
        UPDATE proces_pedido
        SET     estado_seguimiento = 1
            WHERE id_proc_pedido = v_id_proc_pedido;
        COMMIT;
		v_salida:=1;
	EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;

    END SP_ProcesoPedidoUpdateSeguimientos;


CREATE OR REPLACE PROCEDURE FERIAFAST.SP_SeguimientoEstadodePedido (v_id_seguimiento NUMBER, v_est_seguimiento VARCHAR2, v_salida OUT NUMBER)

    AS 
    BEGIN
        UPDATE seguimiento
        SET     est_seguimiento = v_est_seguimiento
            WHERE id_seguimiento = v_id_seguimiento;
        COMMIT;
		v_salida:=1;
	EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;

    END SP_SeguimientoEstadodePedido;
	
	