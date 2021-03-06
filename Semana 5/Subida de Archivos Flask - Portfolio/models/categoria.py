from sqlalchemy.orm import relationship
from config.base_datos import bd
from sqlalchemy import Column, types
from sqlalchemy.schema import ForeignKey

class CategoriaModel(bd.Model):
    __tablename__='t_categoria'
    categoriaId = Column(
        name='cat_id',
        type_=types.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    categoriaNombre = Column(
        name='cat_nombre',
        type_=types.String(45),
        nullable=False
    )
    categoriaOrden = Column(
        name='cat_orden',
        type_=types.Integer,
        nullable=False
    )
    categoriaEstado = Column(
        name='cat_estado',
        type_=types.Boolean(),
        # el default es el valor por defecto si es que no se ingresa uno
        default=True, 
        nullable=False
    )
    # FK
    usuario = Column(
        ForeignKey('t_usuario.usuario_id'),
        name='usuario_id',
        type_=types.Integer,
        nullable=False
    )
    # el parametro cascade sirve para indicar que va a suceder cuando se elimine un padre, en este caso al poner 'all, delete', todos los hijos se van a eliminar consecuentemente
    # https://docs.sqlalchemy.org/en/14/orm/cascades.html
    conocimientos = relationship('ConocimientoModel', backref='categoriaConocimientos', cascade='all, delete')

    def __init__(self, nombre, orden, estado, usuario ):
        self.categoriaNombre = nombre
        self.categoriaOrden = orden
        self.usuario = usuario
        if estado: 
            self.categoriaEstado = estado
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()
    
    def delete(self):
        bd.session.delete(self)
        bd.session.commit()

    def json(self):
        return {
            'cat_id': self.categoriaId,
            'cat_nombre': self.categoriaNombre,
            'cat_orden':self.categoriaOrden,
            'cat_estado': self.categoriaEstado
        }