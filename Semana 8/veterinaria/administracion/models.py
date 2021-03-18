from django.db import models


# Para ver todos los tipos de los modelos:
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
# Para ver todos los tipos de datos que se pueden usar en django:
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types

class EspecieModel(models.Model):
    especieId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='especie_id'
    )
    especieNombre = models.CharField(
        max_length=45,
        null=False,
        db_column="especie_nombre"
    )

    def __str__(self):
        """Sirve para modificar la forma en la cual se mostrara el objeto por consola"""
        return self.especieNombre

    class Meta:
        db_table = 't_especie'
        # los siguientes atributos solamente sirven si vamos a utilizar el panel administrativo
        # es la forma en la cual se mostrara ese modelo en el panel administrativo
        verbose_name = 'Especie'
        # es la forma en la cual se mostrara el nombre en plural
        # verbose_name_plural = 'Especies'


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
    # al momento de eliminar un padre, tenemos que indicar que va a pasar con sus hijos:
    # CASCADE => permite eliminar al padre y consecuentemente eliminar a los hijos tambien.
    # PROTECT => no permite eliminar al padre mientras que tenga hijos (primero se eliminaria a los hijos y luego al padre)
    # SET_NULL => permite eliminar al padre y luego a sus hijos le cambiara el valor a NULL, sus hijos se quedan sin padre 😢
    # DO_NOTHING => permite eliminar al padre y deja su pk sin modificar en los hijos, esto generara una mala integridad de los datos ya que los hijos seguiran apuntando al padre pero este ya no existe
    # RESTRICT => no permite la eliminacion y lanzara un error de tipo RestrictedError, muy similar al PROTECT
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    especie = models.ForeignKey(
        to=EspecieModel,
        on_delete=models.PROTECT,
        # el related_name sirve para cuando querramos ingresar a su relacion inversa
        related_name='especiesRaza',
        db_column='especie_id',
        verbose_name='Especie',
        help_text='Id de la especie'
    )

    def __str__(self):
        return self.razaNombre

    # para definir algunas opciones extras como el nombre de la tabla, el ordenamiento de los resultados y modificar opciones de visualizacion en el panel administrativo se crea una clase Meta que sirve para pasar los metadatos al padre (a la clase que hemos heredado)

    class Meta:
        # asi se cambia el nombre de la tabla
        db_table = 't_raza'
        verbose_name = 'raza'


class ClienteModel(models.Model):
    clienteDni = models.CharField(
        unique=True,
        null=False,
        primary_key=True,
        max_length=9,
        db_column='cli_dni'
    )
    clienteNombre = models.CharField(
        max_length=45,
        db_column='cli_nombre',
        null=False
    )
    clienteApellido = models.CharField(
        max_length=45,
        db_column='cli_apellido',
        null=False
    )
    clienteEmail = models.EmailField(
        max_length=45,
        db_column='cli_email',
        null=False
    )
    clienteFono = models.CharField(
        max_length=10,
        db_column='cli_fono',
        null=False
    )

    # https://docs.djangoproject.com/en/3.1/ref/models/options/
    class Meta:
        db_table = 't_cliente'
        verbose_name = 'Cliente'


class MascotaModel(models.Model):
    SEXO_CHOICES = [
        ('M', 'MACHO'),
        ('H', 'HEMBRA')
    ]
    mascotaId = models.AutoField(
        primary_key=True,
        db_column='mascota_id',
        null=False,
        unique=True
    )
    mascotaNombre = models.CharField(
        max_length=45,
        db_column='mascota_nombre',
        null=False
    )
    mascotaFechaNacimiento = models.DateField(
        db_column='mascota_fecnac',
        null=False
    )
    mascotaSexo = models.CharField(
        max_length=1,
        db_column='mascota_sexo',
        choices=SEXO_CHOICES,
        default='M',
        null=False
    )
    cliente = models.ForeignKey(
        to=ClienteModel,
        on_delete=models.PROTECT,
        db_column='cli_dni',
        related_name='mascotasCliente',
        null=False
    )
    raza = models.ForeignKey(
        to=RazaModel,
        on_delete=models.PROTECT,
        db_column='raza_id',
        related_name='mascotasRaza',
        null=False
    )

    class Meta:
        db_table = 't_mascota'
        verbose_name = 'Mascota'


class PromocionModel(models.Model):
    promocionId = models.AutoField(
        primary_key=True,
        db_column='promo_id',
        unique=True,
        null=False
    )
    promocionDescripcion = models.CharField(
        max_length=45,
        db_column='promo_descripcion',
        null=False
    )
    promocionEstado = models.BooleanField(
        default=True,
        db_column='promo_estado',
        null=False
    )

    def __str__(self):
        return "La promocion es: {} y su estado es: {}".format(self.promocionDescripcion, self.promocionEstado)

    class Meta:
        db_table = 't_promocion'
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'


class HistorialModel(models.Model):
    historialId = models.AutoField(
        primary_key=True,
        db_column='historial_id',
        null=False,
        unique=True
    )
    historialCanje = models.BooleanField(
        db_column='historial_canje',
        default=True,
        null=False
    )
    mascota = models.ForeignKey(
        to=MascotaModel,
        db_column='mascota_id',
        null=False,
        on_delete=models.PROTECT,
        related_name='historialesMascota'
    )
    promocion = models.ForeignKey(
        to=PromocionModel,
        db_column='promo_id',
        null=False,
        on_delete=models.PROTECT,
        related_name='historialesPromocion'
    )

    class Meta:
        db_table = 't_historial'
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'
