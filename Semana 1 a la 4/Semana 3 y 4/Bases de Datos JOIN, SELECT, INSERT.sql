create database bdprueba;
create schema bdprueba;
use bdprueba;
create table t_alumno(
# Solamente puede haber un campo en una tabla que sea auto incrementable
	alumno_id int auto_increment not null primary key,
    alumno_nombre varchar(35),
    alumno_fecnac date,
    alumno_email varchar(25),
    alumno_dni varchar(8)
);

# La forma correcta de inserta datos a una tabla es:
insert into t_alumno (alumno_nombre, alumno_fecnac, alumno_email, alumno_dni) values
					('Eduardo','1985-08-01','ederiveroman@gmail.com','73500746');

insert into t_alumno (alumno_fecnac, alumno_nombre, alumno_dni, alumno_email) values
					('2000-01-15','Juan Martin','71500746','jmartin@gmail.com');

insert into t_alumno (alumno_fecnac, alumno_nombre, alumno_dni) values
					('2000-03-15','Rosa Fiorella','71234746');

# la forma para visualizar la informacion de una o mas tablas
select alumno_nombre, alumno_fecnac from t_alumno;
select * from t_alumno;
# la forma de usar condicionales en bases de datos es luego de indicar las tablas usamos la clausula where
select * from t_alumno where alumno_nombre = 'Eduardo';
# select : seleccionar los siguientes campos
# campos | * si usamos el asterisco indica que va a devolver todos los campos de las tablas
# from : indicar desde que tabla o tablas queremos devolver
# tablas: minimo una tabla
# ADICIONALMENTE where: nos sirve para indicar ciertas restricciones de filtro

# CREAR UNA TABLA de habilidades en la cual se guarde la descripcion de la habilidad y su nivel
CREATE TABLE t_habilidad(
	habilidad_id int auto_increment not null primary key,
    habilidad_descripcion varchar(100),
    habilidad_nivel varchar(15),
    alumno_id int not null,
    foreign key (alumno_id) references t_alumno(alumno_id)
);

# 5 registros de habilidades 
insert into t_habilidad (habilidad_descripcion, habilidad_nivel, alumno_id) values 
						('ESTUDIOSO','ALTO',1),
                        ('HIPERACTIVO','MEDIO',2),
                        ('DEPORTISTA','BAJO',3),
                        ('ESTUDIOSO','MEDIO',2),
                        ('CIENTIFICO','ALTO',1);

SELECT * FROM T_HABILIDAD;
SELECT * FROM T_HABILIDAD INNER JOIN 
T_ALUMNO ON T_HABILIDAD.ALUMNO_ID = T_ALUMNO.ALUMNO_ID;

# CREAR UNA BASE DE DATOS BDEMPRESA EN EL CUAL SE TENGA DOS TABLAS UNA DEPARTAMENTO Y OTRA 
# EMPLEADO,
# EN LA TABLA DEPARTAMENTO DEBE IR EL NOMB_DEP, NIVEL; Y EN LA TABLA EMPLEADO DEBE IR EL NOMBRE,
# APELLIDO Y NUM_CONTRATO E INDICAR LA RELACION QUE DEBE DE TENER ESAS DOS TABLAS;

CREATE DATABASE BDEMPRESA;
USE BDEMPRESA;
create table t_departamento(
	dep_id int auto_increment not null,
    dep_nomb varchar(25),
    dep_nivel int,
    primary key(dep_id)
);
create table t_empleado(
	emp_id int auto_increment not null primary key,
    emp_nomb varchar(30),
    emp_apellido varchar(45),
    emp_numcont varchar(5),
    dep_id int,
    foreign key (dep_id) references t_departamento(dep_id)
);

insert into t_departamento (dep_nomb, dep_nivel) values
							('Ventas',1),
                            ('Administracion',2),
                            ('Finanzas',2),
                            ('Marketing',3);

insert into t_empleado (emp_nomb, emp_apellido, emp_numcont, dep_id) values
						('juancho','rodriguez','0007',2),
                        ('rosa','martinez','0010',1),
                        ('hugo','mendieta','0145',3),
                        ('estaban','quito','0146',2),
                        ('eduardo','amado','1474',3),
                        ('roxana','obando','1245',NULL);

# AS: es para poner alias a las columnas, a las tablas e inclusive a algunas funciones
SELECT * FROM t_departamento as dep inner join t_empleado as emp on dep.dep_id = emp.dep_id;

# LEFT JOIN (devuelve todo el universo de la izquierda y la interseccion del universo de la derecha)
SELECT * FROM t_departamento as dep left join t_empleado as emp on dep.dep_id = emp.dep_id;

# RIGHT JOIN (devuelve todo el universo de la derecha y la interseccion del universo de la izquierda)
SELECT * FROM t_departamento as dep right join t_empleado as emp on dep.dep_id = emp.dep_id;

# FULL OUTER JOIN (devuelve una union entre el universo de la izquierda y el de la derecha)
SELECT * FROM t_departamento as dep left join t_empleado as emp on dep.dep_id = emp.dep_id union
SELECT * FROM t_departamento as dep right join t_empleado as emp on dep.dep_id = emp.dep_id;



