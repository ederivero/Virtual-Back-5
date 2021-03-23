# aca declararemos todas las rutas de la aplicacion administracion
from django.urls import path
from .views import (EspeciesController,
                    EspecieController,
                    RazasController,
                    MascotasController,
                    prueba,
                    CustomController,
                    BusquedaController,
                    ClienteController,
                    contabilitar_sexo)
# esta variable se tiene que llamar asi SI O SI
urlpatterns = [
    path('especie', EspeciesController.as_view()),
    path('especie/<int:id>', EspecieController.as_view()),
    path('raza', RazasController.as_view()),
    path('mascota', MascotasController.as_view()),
    path('prueba', prueba),
    path('prueba2', CustomController.as_view()),
    path('busquedaFecha', BusquedaController.as_view()),
    path('contabilizarSexo', contabilitar_sexo),
    path('cliente', ClienteController.as_view()),
]
