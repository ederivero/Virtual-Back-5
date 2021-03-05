from config.base_datos import bd
from sqlalchemy import Column, types
from sqlalchemy.schema import ForeignKey

class ConocimientoModel(bd.Model):
    __tablename__ = 't_conocimiento'
    conocimientoId = Column(
        name='conocimiento_id',
        type_=types.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False
    )
    conocimientoTitulo = Column(
        name='conocimiento_titulo',
        type_=types.String(45),
        nullable=False
    )
    conocimientoPuntuacion = Column(
        name='conocimiento_puntuacion',
        type_=types.DECIMAL(2,1),
        nullable=False
    )
    conocimientoImagenTN = Column(
        name='conocimiento_imagen_thumbnail',
        type_=types.TEXT,
        nullable=False
    )
    conocimientoImagenLarge = Column(
        name='conocimiento_imagen_large',
        type_=types.TEXT,
        nullable=False
    )
    conocimientoDescripcion = Column(
        name='conocimiento_descripcion',
        type_=types.String(200),
        nullable=False
    )
    # FK
    categoria = Column(
        ForeignKey('t_categoria.cat_id'),
        name='cat_id',
        type_=types.Integer,
        nullable=False
    )

    def __init__(self, titulo, puntuacion, imagentn, imagenl, descripcion, categoria):
        self.conocimientoTitulo = titulo
        self.conocimientoPuntuacion = puntuacion
        self.conocimientoImagenTN = imagentn
        self.conocimientoImagenLarge = imagenl,
        self.conocimientoDescripcion = descripcion
        self.categoria = categoria
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()