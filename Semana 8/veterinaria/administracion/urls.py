# aca declararemos todas las rutas de la aplicacion administracion
from django.urls import path
from .views import EspeciesController, EspecieController
# esta variable se tiene que llamar asi SI O SI
urlpatterns = [
    path('especie', EspeciesController.as_view()),
    path('especie/<int:id>', EspecieController.as_view()),
]
