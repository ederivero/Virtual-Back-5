use playa_estacionamiento;
show tables;
insert into t_vehiculo (veh_placa, veh_marca, veh_modelo, veh_color, veh_anio) values
						('V3A527','VOLKSWAGEN','TIGUAN','BLANCO','2018'),
						('ABC345','FORD','FIESTA','AMARILLO','2015'),
						('T4F567','RENAULT','KOLEOS','NEGRO','2018'),
						('AVF465','DAEWOO','TICO','AZUL','2016'),
						('GNB867','HIUNDAY','SANTA FE','NEGRO','2018');

insert into t_playa (playa_nomb, playa_capacidad) values 
					('CALLE SAN FRANCISCO 204',30),
					('SAN JUAN DE DIOS 132',25),
					('AV EEUU 505',10);
insert into t_registro (veh_id, playa_id, reg_fechin, reg_fechfin, reg_monto) values
						(1,1,'2020-11-05 10:20','2020-11-05 11:33', 10.50),
						(1,2,'2020-11-02 17:20','2020-11-02 19:33', 12),
						(2,1,'2020-11-04 10:20','2020-11-04 11:33', 14),
						(3,1,'2020-11-04 10:20','2020-11-04 11:33', 8),
						(3,3,'2020-11-05 10:05','2020-11-05 11:33', 6),
						(4,3,'2020-11-01 10:25','2020-11-01 11:33', 4.50),
						(4,3,'2020-11-01 19:34','2020-11-01 20:45', 4.50),
						(5,1,'2020-10-05 10:20','2020-10-05 11:33', 10.50),
						(5,2,'2020-10-05 10:20','2020-10-05 11:33', 10.50),
						(1,1,'2020-10-05 10:20','2020-10-05 11:33', 5);
						