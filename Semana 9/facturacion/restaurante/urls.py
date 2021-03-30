from django.urls import path
# si queremos importar todo de un archivo ponemos el *
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('plato', PlatosController.as_view()),
    path('plato/<int:id>', PlatoController.as_view()),
    path('registro', RegistrarPersonalController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh_token', TokenRefreshView.as_view()),
    path('login_custom', CustomPayloadController.as_view()),
    path('mesa', MesaController.as_view()),
    path('notapedido', NotaPedidoController.as_view()),
    path('mozo/mesas', MostrarMesasMozoController.as_view()),
    path('comprobante/<int:id_comanda>',
         GenerarComprobantePagoController.as_view()),
]
