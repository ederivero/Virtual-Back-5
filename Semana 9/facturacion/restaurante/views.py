from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response


class PlatosController(generics.ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def get(self, request):
        return Response({
            'success': True
        })

    def post(self, request):
        return Response({
            'success': True
        })
