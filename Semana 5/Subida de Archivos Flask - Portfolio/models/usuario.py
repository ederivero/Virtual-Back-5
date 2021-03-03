from config.base_datos import bd
from sqlalchemy import Column, types

class UsuarioModel(bd.Model):
    __tablename__="t_usuario"
    usuarioId = Column(
        name='usuario_id',
        type_=types.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
        )
    usuarioNombre = Column(
        name='usuario_nombre',
        type_=types.String(25),
        nullable=False
    )
    usuarioApellido = Column(
        name='usuario_apellido',
        type_=types.String(45),
        nullable=False
    )
    usuarioCorreo = Column(
        name='usuario_correo',
        type_=types.String(45),
        nullable=False
    )
    usuarioPassword = Column(
        name='usuario_password',
        type_=types.TEXT,
        nullable=False
    )
    usuarioFoto = Column(
        name='usuario_foto',
        type_=types.TEXT,
        nullable=False
    )
    usuarioTitulo = Column(
        name='usuario_titulo',
        type_=types.String(45),
        nullable=False
    )
    usuarioInfo = Column(
        name='usuario_info',
        type_=types.TEXT,
        nullable=False
    )
    usuarioCV = Column(
        name='usuario_cv',
        type_=types.TEXT,
        nullable=False
    )
    usuarioSuperUser = Column(
        name='usuario_superuser',
        type_=types.Boolean(),
        nullable=False
    )

    def __init__(self, nombre, apellido, correo, password, titulo, informacion, curriculum, superusuario):
        self.usuarioNombre = nombre
        self.usuarioApellido = apellido
        self.usuarioCorreo = correo
        self.usuarioTitulo = titulo
        self.usuarioInfo = informacion
        self.usuarioCV = curriculum
        self.usuarioSuperUser = superusuario
        self.usuarioPassword = password
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()
