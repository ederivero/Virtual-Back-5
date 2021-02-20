from config.base_datos import bd


class CategoriaModel(bd.Model):
    __tablename__ = "t_categoria"
    categoriaId = bd.Column(name="categoria_id", type_=bd.Integer,
                            primary_key=True, autoincrement=True, nullable=False, unique=True)
    categoriaDescripcion = bd.Column(
        name="categoria_descripcion", type_=bd.String(45), unique=True, nullable=False)
