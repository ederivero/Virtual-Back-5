from django.urls import path
# si queremos importar todo de un archivo ponemos el *
from .views import *

urlpatterns = [
    path('plato', PlatosController.as_view()),
]
