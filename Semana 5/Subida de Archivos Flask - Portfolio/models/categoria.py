from config.base_datos import bd
from sqlalchemy import Column, types

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
    def __init__(self, nombre, orden, estado ):
        self.categoriaNombre = nombre
        self.categoriaOrden = orden
        if estado: 
            self.categoriaEstado = estado
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()