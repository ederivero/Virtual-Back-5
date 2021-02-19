# Para crear una base de datos:
create database bdprueba;
# SOLO EN MYSQL
# create schema bdprueba;

# para utilizar esa base de datos:
use bdprueba;

# para crear una tabla:
create table t_categoria(
# Solamente puede haber una columna en una tabla que sea auto increment
	categoria_id int primary key not null auto_increment,
    categoria_nombre varchar(25) unique
);

# para eliminar una tabla:
drop table t_categoria;
# para eliminar una base de datos:
# drop database elecciones;

# hacer la creacion de la tabla producto sin la llave foranea (FK)
# el nombre debe ser unico, y todos los campos no deben admitir 
# valores nulos
use bdprueba;
show tables;

CREATE tAbLe t_producto(
	producto_id int not null primary key auto_increment,
    producto_nombre varchar(25) not null unique,
    producto_precio float(5,2) not null,
    producto_cantidad int not null,
    categoria_id  int not null,
    # foreign key (nombre_columna) references t_tabla(primary_key)
    foreign key (categoria_id) references t_categoria(categoria_id)
);

# crear registros:
insert into t_categoria (categoria_nombre) values ('Abarrotes');
insert into t_categoria (categoria_nombre) values 	('Pastas'),
													('Limpieza'),
													('Mascotas'),
													('Higiene');

# insert into t_categoria (categoria_nombre) values ('Abarrotes');
# si no quiero indicar que columnas voy a registar voy a tener que ingresar absolutamente todas las 
# columnas incluyendo la pk y todo
insert into t_producto values (1, 'Lejia', 3.40, 50, 1);
insert into t_producto values (50, 'Canelon', 1.80, 25, 2);
insert into t_producto (producto_nombre, producto_precio, producto_cantidad, categoria_id) values
					   ('Ricodog 1kh'  ,  5.40,			  15,			     4),
                       ('Pasta dental' ,  3.80,			  20,			     5);

# no se puede insertar un registro con una llave foranea (fk) que no existe! sino dara el error 1452
#insert into t_producto (producto_nombre, producto_precio, producto_cantidad, categoria_id) values
#						('Paneton sin gluten', 22.40, 15, 50);
select * from t_categoria;
# para ver los datos registrados:
select producto_id, producto_nombre, producto_precio, producto_cantidad, categoria_id  from t_producto;

# si queremos ver todas las columnas de una tabla o tablas
select * from t_producto;
select * from t_categoria;

insert into t_categoria (categoria_nombre) values ('Otros');
select * from t_categoria;
# los joins! => inner join, left join, right join, full outer join
select * from t_producto inner join t_categoria on t_producto.categoria_id = t_categoria.categoria_id;

select * from t_producto right join t_categoria on t_producto.categoria_id = t_categoria.categoria_id;

select * from t_producto left join t_categoria on t_producto.categoria_id = t_categoria.categoria_id;









