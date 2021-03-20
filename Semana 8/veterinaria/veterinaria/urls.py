from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestion de Veterinaria",
        default_version="1.0",
        description="API usando DRF para el manejo de las mascotas de una veterinaria",
        terms_of_service="http://www.google.com",
        contact=openapi.Contact(name="Eduardo de Rivero",
                                email="ederiveroman@gmail.com"),
        # para una mayor info sobre las licencias, mira: https://es.wikipedia.org/wiki/Licencia_de_software
        license=openapi.License(
            name="MIT", url="https://es.wikipedia.org/wiki/Licencia_MIT")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('', schema_view.with_ui('swagger')),
    path('redoc', schema_view.with_ui('redoc')),
    path('admin/', admin.site.urls),
    path('', include('administracion.urls')),
]
