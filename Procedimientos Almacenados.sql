create or replace procedure sp_listar_ordenes(ordenes out sys_refcursor)
is

begin
open ordenes for select * from restaurant_orden;
end;

create or replace procedure sp_listar_platos(platos out sys_refcursor)
is

begin
open platos for select * from restaurant_plato;
end;


create or replace procedure sp_agregar_orden(
    v_nombre varchar2,
    v_precio number,
    v_plato_id number,
    v_salida out number
) is

begin
    insert into restaurant_orden(nombre, precio, plato_id) 
    values(v_nombre, v_precio, v_plato_id);
    commit;
    v_salida:=1;

    exception

    when others then
    v_salida:=0;
end;
