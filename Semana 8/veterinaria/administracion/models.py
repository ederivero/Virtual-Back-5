from django.db import models

# Para ver todos los tipos de los modelos:
# https://docs.djangoproject.com/en/3.1/ref/models/fields/


class RazaModel(models.Model):
    # si yo no defino la primary key esta se creara automaticamente en mi bd con el nombre de columa <id>
    # solamente una columna por tabla puede ser autofield (autoincrementable)
    razaId = models.AutoField(
        primary_key=True,  # indica que sera primary key
        # indica que se generara automaticamete (es redundante)
        auto_created=True,
        unique=True,  # va a ser unico y su valor no se repetira
        null=False,  # no puede quedarse sin informacion
        db_column='raza_id',  # su nombre de columna en la bd sera diferente
        # campos para el uso del lado administrativo:
        help_text='Aca va el id',  # es un campo de ayuda
        verbose_name='Id de la raza'  # la descripcion de esa columna
    )
    razaNombre = models.CharField(
        max_length=45,  # al usar charField tenemos que obligatoriamente poner la longitud
        db_column='raza_nombre',
        verbose_name='Nombre de la raza'
    )
    # para definir algunas opciones extras como el nombre de la tabla, el ordenamiento de los resultados y modificar opciones de visualizacion en el panel administrativo se crea una clase Meta que sirve para pasar los metadatos al padre (a la clase que hemos heredado)

    class Meta:
        # asi se cambia el nombre de la tabla
        db_table = 't_raza'
