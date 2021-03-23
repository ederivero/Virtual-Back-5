# Tipos de datos
# https://dev.mysql.com/doc/refman/8.0/en/data-types.html
# Numericos
# int que acepta valores desde -2147483648 hasta 2147483647
# tinyint (bool) entero que acepta valores de -128 a 127, cuando solamente 
# ingreso un valor (1 o 0) este se convierte internamente en bool
# bool => internamente se creara como un tinyint que admitira valores 0 o 1
# smallint: acepta valores entre -32768 hasta 32767
# float(m, d): m => es la cantidad de numeros en total que vamos a tener (parte entera
# parte decimal, d=> la cantidad de decimales que vamos a tener en nuestra columna

# Tiempo y fecha
# date: su formato es YYYY-MM-DD desde el 1000-01-01 hasta el 9999-12-31
# datetime: su formato es YYYY-MM-DD HH:MM:SS
# timestamp: no guarda ni guiones ni dos puntos ni espacios YYYYMMDDHHMMSS
# time: HH:MM:SS

# String 
# char(lng): recibe un parametro el cual va a ser la longitud para almacenar en esa 
#columna
# varchar(lng): recibe un parametro en el cual va a ser la longitud MAXIMA para 
# almacenar los datos
# text: es un tipo de dato que acepta hasta almacenar 65535 caracteres, generalmente
# se usa para almacenar textos muy grandes y contraseñas

# para crear una base de datos en mi servidor:
create database bdPrueba;
# create schema bdPrueba;

# sirve para mostrar todas las bases de datos del servidor.
show databases;

# sirve para indicar en que base de datos voy a trabajar
use bdPrueba;

# Para nosotros crear una tabla necesitamos saber:
# * nombre de la tabla
# * nombre de los campos o atributos
# * la definicion de cada campo
#create table nomb_tabla (
#	nombre_columna tipo_columna *algunas_configuraciones_extras
#)
#not null => para evitar que al momento de ingresar un registro, 
#			esa columna pueda carecer de informacion
#auto_increment  => esto va de la mano con el tipo de dato int puesto que al ser entero 
#					va a ser autoincrementable y generalmente se usa en las primary keys.
#primary key => es usada para definir que la columna va a ser la llave primaria de la tabla
#				por lo que debe ser unica e irrepetible y generalmente debe ser int.

