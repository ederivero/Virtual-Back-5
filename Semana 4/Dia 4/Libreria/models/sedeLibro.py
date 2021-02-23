from sqlalchemy.sql.schema import ForeignKey
from config.base_datos import bd
from sqlalchemy import Column, types
class SedeLibroModel(bd.Model):
    __tablename__="t_sede_libro"
    sedeLibroId = Column(name='sede_libro_id', type_=types.Integer, primary_key=True, autoincrement=True, unique=True)
    # es exactamente lo mismo usar bd.Column que llamar a Column() de sqlalchemy la diferencia es que nos brinda ayuda
    int
    sede = Column(ForeignKey('t_sede.sede_id'), name='sede_id', type_=types.Integer)
    libro = Column(ForeignKey('t_libro.libro_id'), name='libro_id', type_=types.Integer)