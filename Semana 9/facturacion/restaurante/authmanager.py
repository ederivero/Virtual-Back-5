from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    """Clase que sirve para modificar el comportamiento del modelo Auth del proyecto de django"""

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
        usuario.save(using=self._db)  # sirve para referenciar a la bd
        return usuario
