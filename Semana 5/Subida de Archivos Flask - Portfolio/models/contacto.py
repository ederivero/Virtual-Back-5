from config.base_datos import bd
from sqlalchemy import Column, types
from sqlalchemy.schema import ForeignKey
from datetime import datetime
class ContactoModel(bd.Model):
    __tablename__='t_contacto'
    contactoId = Column(
        name='contacto_id',
        nullable=False,
        type_=types.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    contactoNombre = Column(
        name='contacto_nombre',
        nullable=False,
        type_=types.String(45)
    )
    contactoEmail = Column(
        name='contacto_email',
        nullable=False,
        type_=types.String(45)
    )
    contactoFono = Column(
        name='contacto_fono',
        nullable=False,
        type_=types.String(10)
    )
    contactoMensaje = Column(
        name='contacto_mensaje',
        nullable=False,
        type_=types.TEXT
    )
    contactoFecha = Column(
        name='contacto_fecha',
        nullable=False,
        default= datetime.now(),
        type_=types.DateTime()
    )
    usuario = Column(
        ForeignKey('t_usuario.usuario_id'),
        name='usuario_id',
        nullable=False,
        type_=types.Integer
    )

    def __init__(self, nombre, correo, telefono, mensaje, usuario):
        self.contactoNombre = nombre
        self.contactoEmail = correo
        self.contactoFono = telefono
        self.contactoMensaje = mensaje
        self.usuario = usuario
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()
    