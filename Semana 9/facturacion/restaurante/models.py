from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authmanager import UsuarioManager


class PersonalModel(AbstractBaseUser, PermissionsMixin):
    """Modelo de la base de datos del personal del sistema"""
    TIPO_PERSONAL = [
        (1, 'ADMINISTRADOR'),
        (2, 'CAJERO'),
        (3, 'MOZO')
    ]
    # si no definimos una PK django creara una automaticamente y le pondra de nombre de columna id
    personalId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='personal_id'
    )
    personalCorreo = models.EmailField(
        db_column='personal_correo',
        max_length=30,
        verbose_name='Correo del personal',
        unique=True
    )
    personalTipo = models.IntegerField(
        db_column='personal_tipo',
        choices=TIPO_PERSONAL,
        verbose_name='Tipo del personal'
    )
    personalNombre = models.CharField(
        max_length=45,
        null=False,
        db_column='personal_nombre',
        verbose_name='Nombre del personal'
    )
    personalApellido = models.CharField(
        max_length=45,
        null=False,
        db_column='personal_apellido',
        verbose_name='Apellido del personal'
    )
    password = models.TextField(
        db_column='personal_password',
        verbose_name='Contraseña del personal'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # aca asignamos el comportamiento con el modelo
    objects = UsuarioManager()
    # ahora indico que columna va a ser la encargada del login
    # hace esa columna unica y null=false
    USERNAME_FIELD = 'personalCorreo'
    # sirve para solicitar los campos al momento de crear el superusuario por consola EXCLUSIVAMENTE
    REQUIRED_FIELDS = ['personalNombre', 'personalTipo', 'personalApellido']

    class Meta:
        db_table = 't_personal'
        verbose_name = 'personal'
        verbose_name_plural = 'personales'


class MesaModel(models.Model):
    mesaId = models.AutoField(
        primary_key=True,
        db_column="mesa_id",
        null=False
    )
    mesaNumero = models.CharField(
        db_column='mesa_numero',
        max_length=10,
        null=False,
        verbose_name='Numero de la mesa'
    )
    mesaCapacidad = models.IntegerField(
        db_column='mesa_capacidad',
        null=False,
        verbose_name='Capacidad de la mesa'
    )
    mesaEstado = models.BooleanField(
        db_column='mesa_estado',
        null=False,
        verbose_name='Estado de la mesa',
        default=True
    )

    class Meta:
        db_table = 't_mesa'
        verbose_name = 'Mesa'


class PlatoModel(models.Model):
    platoId = models.AutoField(
        primary_key=True,
        db_column='plato_id',
        null=False
    )
    platoDescripcion = models.CharField(
        db_column='plato_descripcion',
        null=False,
        verbose_name='Nombre del plato',
        max_length=50
    )
    platoCantidad = models.IntegerField(
        db_column='plato_cantidad',
        verbose_name='Cantidad de los platos',
        null=False
    )
    platoFoto = models.ImageField(
        db_column='plato_foto',
        verbose_name='Foto del plato',
        null=False
    )
    platoPrecio = models.DecimalField(
        db_column='plato_precio',
        max_digits=5,
        decimal_places=2,
        null=False,
        verbose_name='Precio del plato'
    )

    class Meta:
        db_table = 't_plato'
        verbose_name = 'Plato'


class PersonalMesaModel(models.Model):
    personalId = models.ForeignKey(
        to=PersonalModel,
        on_delete=models.CASCADE,
        related_name='personalMesas',
        db_column='personal_id'
    )
    mesaId = models.ForeignKey(
        to=MesaModel,
        on_delete=models.CASCADE,
        related_name='mesaPersonales',
        db_column='mesa_id'
    )

    class Meta:
        db_table = 't_personal_mesa'
        verbose_name = 'personal mesa'


class ComprobanteModel(models.Model):
    pass


class CabeceraComandaModel(models.Model):
    cabeceraId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='cabecera_id'
    )
    cabeceraFecha = models.DateField(
        db_column='cabecera_fecha',
        null=False
    )
    cabeceraTotal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        db_column='cabecera_total',
        null=False
    )
    cabeceraCliente = models.TextField(
        db_column='cabecera_cliente',
        null=False
    )
    mozo = models.ForeignKey(
        to=PersonalModel,
        on_delete=models.PROTECT,
        db_column='mozo_id',
        null=False
    )
    mesa = models.ForeignKey(
        to=MesaModel,
        on_delete=models.PROTECT,
        db_column='mesa_id',
        null=False
    )
    comprobante = models.OneToOneField(
        to=ComprobanteModel,
        db_column='comprobante_id',
        null=False

    )
