from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    """Clase que sirve para modificar el comportamiento del modelo User del proyecto de django"""

    def create_user(self, email, nombre, apellido, tipo, password=None):
        """Creacion de un usuario comun y corriente"""
        if not email:
            raise ValueError(
                "El usuario debe tener obligatoriamente un correo")
        # normalizo el email que aparte de validar si hay un @ y un . esta funcionalidad lo lleva todo a lowecase (minusculas) y quita todos los espacios que pudiesen haber
        email = self.normalize_email(email)
        # creo mi objeto de usuario pero aun no lo guardo en la bd
        usuario = self.model(personalCorreo=email, personalNombre=nombre,
                             personalApellido=apellido, personalTipo=tipo)
        # ahora encriptamos la contraseña
        usuario.set_password(password)
        # guardamos en la bd
        # sirve para referenciar a la bd en el caso que nosotros tengamos varias bd
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, personalCorreo, personalNombre, personalApellido, personalTipo, password):
        """Creacion de un nuevo super usuario para que pueda acceder al panel administrativo y algunas opciones adicionaes"""
        usuario = self.create_user(
            personalCorreo, personalNombre, personalApellido, personalTipo, password)
        # ahora como es un super usuario y para que pueda ingresar al panel administrativo tenemos que designar sus permisos
        # este campo se crea automaticamente por la herencia del user model
        # sirve para poder manipular a otros usuarios y tener permisos exclusivos en el panel administrativo
        usuario.is_superuser = True
        usuario.is_staff = True  # sirve para poder ingresar al panel administrativo
        usuario.save(using=self._db)
