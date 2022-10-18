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

CREATE OR REPLACE PROCEDURE FASTFERIA.SP_AGREGAR_PRODUCTO(
    v_nom_prod VARCHAR2,
    v_precio_prod NUMBER,
    v_desc_prod VARCHAR2,
    v_stock_prod NUMBER,
    v_usuarios_rut VARCHAR2,
    v_blob BLOB,
    v_salida OUT NUMBER,
)
IS 
BEGIN
    INSERT INTO productos(nom_prod, precio_prod, desc_prod, stock_prod, usuarios_rut, foto)
    VALUES(v_nom_prod, v_precio_prod, v_desc_prod, v_stock_prod, v_usuarios_rut, v_blob);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;