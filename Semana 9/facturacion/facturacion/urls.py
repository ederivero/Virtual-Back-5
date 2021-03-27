"""facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

documentation_view = get_schema_view(
    info=openapi.Info(
        title='Facturacion y manejo de restaurantes',
        default_version='1.0',
        description='Facturacion API',
        contact=openapi.Contact(
            email='ederiveroman@gmail.com', name='Eduardo de Rivero'),
    ),
    public=True,
    permission_classes=[AllowAny, ]
)


urlpatterns = [
    path('api/docs', documentation_view.with_ui('swagger')),
    path('api/docs/redoc', documentation_view.with_ui('redoc')),
    path('admin/', admin.site.urls),
    path('', include('restaurante.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# el metodo static sirve para indicar una serie de rutas staticas (solamente para mostrar info ) en el cual se indica el prefijo (la ruta) y luego que documento se mostrara
