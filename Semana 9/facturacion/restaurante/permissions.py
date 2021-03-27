from rest_framework.permissions import BasePermission, SAFE_METHODS


class soloAdministrador(BasePermission):
    def has_permission(self, request, view):
        """Esto es un middleware"""
        # el request nos dara los mismos atributos que nos da el request de las vistas genericas
        # en los customs permissions tenemos que retorna SIEMPRE un booleano (true o false) porque si es verdero procedera con el siguiente permiso o con el controlador final
        print(SAFE_METHODS)
        # SAFE_METHODS son GET, HEAD, OPTIONS
        print(request.user.personalTipo)
        if request.user.personalTipo == 1:
            return True
        else:
            return False
        # if request.method in SAFE_METHODS:
        #     return True
        # else:
        #     return False

# hacer un permiso para los platos que solamente se necesite una token para el metodo post y que solamente un administrador pueda registrar un plato.


class administradorPost(BasePermission):
    def has_permission(self, request, view):
        print(request)
        if request.method == 'POST':
            if request.user.personalTipo == 1:
                return True
            else:
                return False
        else:
            return True


class soloMozos(BasePermission):
    """Permiso para que solamente los mozos puedan acceder"""

    def has_permission(self, request, view):
        # solamente pueden ser mozos
        if request.user.personalTipo == 3:
            return True
        return False
