# crear una BD llamada MUCHOSAMUCHOS
# crear una tabla alumno que tenga su id_alumno, nombre, apellido, grado, fecha de nacimiento y una tabla curso que tenga
# id_curso, nombre_curso, dificultad y una relacion de muchos a muchos
# para la tabla alumno ingresar
#	id_alumno	nombre			apellido	grado	fec_nac
#	001			Eduardo			Juarez		Quinto	1992-08-01
#	002			Christopher		Rodriguez	Cuarto	1993-07-10
#	003			Raul			Pinto		Primero	1996-02-05
#	004			Cristina		Espinoza	Quinto	1992-10-21
#	005			Valeria			Acevedo		Cuarto	1993-05-18
# para la tabla curso ingresar
#	id_curso	nom_curso		dificultad
#	001			Matematica I	Facil
#	002			Fisica I		Facil
#	003			Matematica II	Intermedio
#	004			CTA				Dificil
#	005			Biologia		Dificil 
# todos los de quinto llevan Fisica I y cta, todos los de cuarto llevan matematica II y Biologia y
# todos los de primero llevan matematica I y matematica II

CREATE DATABASE MUCHOSAMUCHOS;
use muchosamuchos;
create table t_alumno(
	alum_id int not null auto_increment primary key,
    alum_nom varchar(40),
    alum_ape varchar(50),
    alum_grado varchar(20),
    alum_fecnac date
);
create table t_curso(
	cur_id int not null auto_increment primary key,
    cur_nom varchar(30),
    cur_dif varchar(30)
);
create table t_alumno_curso(
	id_alumno_curso int not null auto_increment primary key,
    alum_id int,
    cur_id int,
    foreign key (alum_id) references t_alumno(alum_id),
    foreign key (cur_id) references t_curso(cur_id)
);

insert into t_alumno (alum_nom, alum_ape, alum_grado, alum_fecnac) values 
					('Eduardo','Juarez','Quinto','1992-08-01'),
					('Christopher','Rodriguez','Cuarto','1993-07-10'),
					('Raul','Pinto','Primero','1996-02-05'),
					('Cristina','Espinoza','Quinto','1992-10-21'),
					('Valeria','Acevedo','Cuarto','1993-05-18');

insert into t_curso (cur_nom, cur_dif) values
					('Matematica I','Facil'),
					('Fisica I','Facil'),
					('Matematica II','Intermedio'),
					('CTA','Dificil'),
					('Biologia','Dificil');

insert into t_alumno_curso (alum_id, cur_id) values 
							(1,2),(4,2), # todos los de quinto llevan Fisica I
							(1,4),(4,4), # todos los de quinto llevan CTA
							(2,3),(5,3), # todos los de cuarto llevan Matematica II
							(2,5),(5,5), # todos los de cuarto llevan Biologia
							(3,1),(3,3); # todos los de primero llevan Matematica I y Matematica II

# hacer una sentencia para que me muestre : 
# nombre_alumno(Nombre)		apellido_alumno(Apellido)		nombre_curso(Curso)
# select alum_nom as 'Nombre del alumno' from t_alumno;

SELECT Alumno.alum_nom as Nombre, Alumno.alum_ape as Apellido, Curso.cur_nom as Curso from t_alumno_curso as Puente 
inner join t_alumno as Alumno on Puente.alum_id = Alumno.alum_id 
inner join t_curso as Curso on Puente.cur_id = Curso.cur_id;


# https://dev.mysql.com/doc/refman/8.0/en/string-functions.html
# select year(alum_fecnac) from t_alumno;
# traer todos los alumnos que nacieron entre 1992 y 1994

SELECT * FROM t_alumno where year(alum_fecnac) >= 1992 and year(alum_fecnac) <= 1994;
