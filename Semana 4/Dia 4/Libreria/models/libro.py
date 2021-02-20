from config.base_datos import bd
# si queremos usar alguna datatype especifico de una base de datos en particular, debemos de importar el dialecto para que solamente funcione en esa base de datos
from sqlalchemy.dialects import mysql

class LibroModel(bd.Model):
    __tablename__ = "t_libro"
    libroId = bd.Column(name="libro_id", type_=bd.Integer,
                        primary_key=True, unique=True, autoincrement=True)
    libroNombre = bd.Column(name="libro_nombre", type_=bd.String(45))
    libroCantidad = bd.Column(name="libro_cant", type_=bd.Integer)
    # YEAR solo funciona en dialecto MySQL
    libroEdicion = bd.Column(name="libro_edicion", type_=mysql.YEAR())
    # Relaciones (fk)
    autor = bd.Column(bd.ForeignKey('t_autor.autor_id'), name="autor_id",
                      type_=bd.Integer, nullable=False)
    categoria = bd.Column(bd.ForeignKey('t_categoria.categoria_id'),
                          name="categoria_id", type_=bd.Integer, nullable=False)
