from config.base_datos import bd


class SedeModel(bd.Model):
    __tablename__ = "t_sede"
    sedeId = bd.Column(name="sede_id", type_=bd.Integer,
                       primary_key=True, autoincrement=True, unique=True)
    sedeUbicacion = bd.Column(name="sede_ubicacion", type_=bd.String(45))
    sedeLatitd = bd.Column(name="sede_latitud", type_=bd.Float(), nullable=False)
    sedeLongitud = bd.Column(name="sede_longitud", type_=bd.Float(), nullable=False)
    
