# crear una BD llamada MUCHOSAMUCHOS
# crear una tabla alumno que tenga su id_alumno, nombre, apellido, grado, 
# fecha de nacimiento 
# una tabla curso que tenga id_curso, nombre_curso, dificultad
create database if not exists MUCHOSAMUCHOS;
use MUCHOSAMUCHOS;
create table if not exists t_alumno(
	alum_id int primary key not null auto_increment,
    alum_nombre varchar(50),
    alum_apellido varchar(50),
    alum_grado varchar(10),
    alum_fec_nacimiento date
);
create table if not exists t_curso(
	cur_id int primary key not null auto_increment,
    cur_nomb varchar(30),
    cur_dificultad varchar(20)
);
# crear la tabla t_alumno_curso con las fk de las tablas alumno y curso
create table if not exists t_alumno_curso(
	alumno_curso_id int not null primary key auto_increment,
    cur_id int,
    alum_id int,
    foreign key (cur_id) references t_curso(cur_id),
    foreign key (alum_id) references t_alumno(alum_id)
);

insert into t_alumno (alum_nombre, alum_apellido, alum_grado, alum_fec_nacimiento) values 
					('Eduardo','Juarez','Quinto','1992-08-01'),
					('Christopher','Rodriguez','Cuarto','1993-07-10'),
					('Raul','Pinto','Primero','1996-02-05'),
					('Cristina','Espinoza','Quinto','1992-10-21'),
					('Valeria','Acevedo','Cuarto','1993-05-18');

insert into t_curso (cur_nomb, cur_dificultad) values
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
		

select alum_nombre as 'nombre del alumno', alum_apellido as 'apellido' 
from t_alumno where alum_nombre='Eduardo';
# clausula de filtro

# traer todos los alumnos que lleven el curso_id 2
# nombre del alumno, apellido del alumno, grado
# HINT: use join
# HINT 2: use la tabla t_alumno_curso
# Tambien que me diga el nombre del curso (usar otro join 👀)
select 	alum_nombre as 'nombre del alumno', 
		alum_apellido as 'apellido del alumno', 
		alum_grado as 'grado',
        cur_nomb as 'curso'
from t_alumno as A inner join t_alumno_curso as C on A.alum_id = C.alum_id
inner join t_curso on t_curso.cur_id = C.cur_id
where C.cur_id=2;