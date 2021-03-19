# aca declararemos todas las rutas de la aplicacion administracion
from django.urls import path
from .views import EspeciesController
# esta variable se tiene que llamar asi SI O SI
urlpatterns = [
    path('especie', EspeciesController.as_view()),
]
