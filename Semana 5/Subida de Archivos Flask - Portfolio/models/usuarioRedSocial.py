from config.base_datos import bd
from sqlalchemy import Column, types
from sqlalchemy.schema import ForeignKey

class UsuarioRedSocial(bd.Model):
    __tablename__='t_usu_rs'
    usuRedSocId = Column(
        name='usu_rs_id',
        type_=types.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    usuRedSocLink = Column(
        name='usu_rs_link',
        type_=types.TEXT,
        nullable=False
    )
    # hacer las FK
    redSocial = Column(
        ForeignKey('t_red_social.rs_id'),
        name='rs_id',
        nullable=False,
        type_=types.Integer
    )
    usuario = Column(
        ForeignKey('t_usuario.usuario_id'),
        name='usuario_id',
        type_=types.Integer,
        nullable=False
    )

    def __init__(self, link, usuario, red_social):
        self.usuRedSocLink = link
        # ....
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()