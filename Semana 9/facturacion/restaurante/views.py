from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response
from uuid import uuid4


class PlatosController(generics.ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def get(self, request):
        respuesta = self.serializer_class(
            instance=self.get_queryset(), many=True)

        return Response({
            'success': True,
            'content': respuesta.data,
            'message': None
        })

    def post(self, request):
        # para ver que archivos me estan mandando puedo ingresar a su atributo FILES dentro de request
        # https://www.django-rest-framework.org/api-guide/requests/#data
        archivo = request.FILES['platoFoto']
        # para ver que tipo de archivo es
        print(archivo.content_type)
        # para ver el nombre del archivo es
        print(archivo.name)
        # para ver el tamaño del archivo expresado en bytes es
        print(archivo.size)
        # sobreescribiendo el nombre del archivo para que no se vuelva a repetir
        # solamente guardar el uuid sin el nombre de la imagen
        # ee2ee0cd-ea63-4baa-9b70-828aa6af0250juane.jpg
        # ee2ee0cd-ea63-4baa-9b70-828aa6af0250.jpg

        request.FILES['platoFoto'].name = str(
            uuid4())+request.FILES['platoFoto'].name
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
                'success': True,
                'message': 'Se registro el plato exitosamente',
                'content': respuesta.data
            })
        else:
            return Response({
                'success': False,
                'message': 'Error al registrar el plato',
                'content': respuesta.errors
            }, status.HTTP_400_BAD_REQUEST)
