CREATE OR REPLACE PROCEDURE FASTFERIA.SP_LISTAR_USUARIOS (usuarios out SYS_REFCURSOR)
IS 
BEGIN
    OPEN usuarios FOR SELECT * FROM usuarios;
END;

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_LISTAR_PRODUCTOS (productos out SYS_REFCURSOR)
IS 
BEGIN
    OPEN productos FOR SELECT * FROM productos;
END;

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_LISTAR_PEDIDO (pedido out SYS_REFCURSOR)
IS 
BEGIN
    OPEN pedido FOR SELECT * FROM pedido;
END;

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_AGREGAR_PRODUCTO(
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

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_AGREGAR_USUARIOS (
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

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_AGREGAR_PEDIDO(
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