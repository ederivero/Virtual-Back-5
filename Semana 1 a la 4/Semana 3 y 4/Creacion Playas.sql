create database if not exists playa_estacionamiento;
use playa_estacionamiento;
create table if not exists t_vehiculo(
	veh_id int primary key not null auto_increment,
    veh_placa varchar(7),
    veh_marca varchar(20),
    veh_anio year,
    veh_modelo varchar(30),
    veh_color varchar(20)
);
create table if not exists t_playa(
	playa_id int primary key not null auto_increment,
    playa_nomb varchar(100),
    playa_capacidad int
);
create table if not exists t_registro(
	reg_id int primary key not null auto_increment,
    reg_fechin datetime,
    reg_fechfin datetime,
    reg_monto decimal(5,2),
    veh_id int,
    playa_id int,
    foreign key (veh_id) references t_vehiculo(veh_id),
    foreign key (playa_id) references t_playa(playa_id)
);