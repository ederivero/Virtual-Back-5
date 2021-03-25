from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response


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
        print(request.FILES['platoFoto'].size)
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
