from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response
from uuid import uuid4
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import *
import os
# nos trae todas las variables que estamos usando en el settings
from django.conf import settings
from datetime import date


class PlatosController(generics.ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, administradorPost]

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
        # opcion 1
        # formato = request.FILES['platoFoto'].name.split('.')[1]
        # nombre=str(uuid4())+'.'+formato
        # request.FILES['platoFoto'].name = nombre
        ###
        # opcion 2
        nombreOriginal = request.FILES['platoFoto'].name
        formato = nombreOriginal[nombreOriginal.find('.'):]
        nombre = str(uuid4())+formato
        request.FILES['platoFoto'].name = nombre
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


class PlatoController(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def get_queryset(self, id):
        return PlatoModel.objects.get(platoId=id)

    def get(self, request, id):
        resultado = self.serializer_class(instance=self.get_queryset(id))
        return Response({
            'success': True,
            'content': resultado.data,
            'message': None
        })

    def put(self, request, id):
        pass

    def delete(self, request, id):
        plato = self.get_queryset(id)
        foto = str(plato.platoFoto)
        try:
            ruta_imagen = settings.MEDIA_ROOT / foto
            os.remove(ruta_imagen)
        except:
            print('Fotografia del plato no existe')
        plato.delete()
        return Response({
            'success': True,
            'content': None,
            'message': 'Plato eliminado'
        })


class RegistrarPersonalController(generics.CreateAPIView):
    serializer_class = RegistroSerializer

    def post(self, request):
        nuevoPersonal = self.serializer_class(data=request.data)
        if nuevoPersonal.is_valid():
            nuevoPersonal.save()
            return Response({
                'success': True,
                'content': nuevoPersonal.data,
                'message': 'Personal creado exitosamente'
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': nuevoPersonal.errors,
                'message': 'Error al crear el nuevo personal'
            }, status.HTTP_400_BAD_REQUEST)


class CustomPayloadController(TokenObtainPairView):
    """Sirve para modificar el claim de nuestra token de acceso"""
    # los permissions_classes sirve para indicar que tipo de usuario puede acceder a este controller
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer


class MesaController(generics.ListCreateAPIView):
    queryset = MesaModel.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [soloAdministrador]
    # IsAdminUser => valida que el usuario que esta tratando de acceder a cualquiera de los metodos sea is_staff
    # IsAuthenticated => valida que la consulta sea dada por una token valida y correcta
    # IsAuthenticatedOrReadOnly => solamente pedira la token en el caso que no sea un metodo de lectura (get)
    # AllowAny => no le importa nada y no pide tokens ni nada

    def get(self, request):
        print(request.user)
        print(request.auth)
        resultado = self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            'success': True,
            'content': resultado.data,
            'message': None
        })

    def post(self, request):
        resultado = self.serializer_class(data=request.data)
        if resultado.is_valid():
            resultado.save()
            return Response({
                'success': True,
                'content': resultado.data,
                'message': 'Mesa creada exitosamente'
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'content': resultado.errors,
                'message': 'Hubo un error al guardar la mesa'
            }, status.HTTP_400_BAD_REQUEST)


class NotaPedidoController(generics.CreateAPIView):
    serializer_class = NotaPedidoCreacionSerializer
    permission_classes = [IsAuthenticated, soloMozos]

    def post(self, request):
        # crear la cabecera
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        print(request.user)
        numeroMesa = data.validated_data['mesa']
        objMesa = MesaModel.objects.filter(mesaId=numeroMesa).first()
        # validar si la mesa esta disponible
        print(objMesa)
        nuevaCabecera = CabeceraComandaModel(
            # si la columna en la bd es tipo date, al momento de guardar datos con hh:mm:ss y SI USAMOS ese registro recien creado nos dara error ya que indicara que no puede mostrar la hh:mm:ss entonces deberemos guardar SOLAMENTE la fecha (YYYY-MM-DD) sin sus horas con date.today()
            cabeceraFecha=date.today(),
            cabeceraTotal=0,
            cabeceraCliente=data.validated_data['cliente'],
            mozo=request.user,
            mesa=objMesa
        )
        nuevaCabecera.save()
        # crear el detalle
        detalle = data.validated_data['detalle']
        print(detalle)
        for detallecomanda in detalle:
            # buscamos el plato
            print(detallecomanda['cantidad'])
            objPlato = PlatoModel.objects.filter(
                platoId=detallecomanda['plato']).first()
            print(objPlato)
            # creamos el detalle del pedido y lo guardamos
            DetalleComandaModel(
                detalleCantidad=detallecomanda['cantidad'],
                detalleSubtotal=detallecomanda['subtotal'],
                plato=objPlato,  # instancia del modelo plato
                cabecera=nuevaCabecera
            ).save()
            # ahora restamos la cantidad del plato segun lo solicitado
            objPlato.platoCantidad = objPlato.platoCantidad - \
                detallecomanda['cantidad']
            # guardamos ese plato con su cantidad modificada en la bd
            objPlato.save()
            # restar la cantidad vendida de los platos
        # inhabilitar la mesa
        # PISTA = ya tengo la nuevaCabecera
        # PISTA#2 = hacerlo en un serializer y solamente pasar la 'nuevaCabecera'
        resultado = MostrarPedidoSerializer(instance=nuevaCabecera)

        return Response({
            'success': True,
            'content': resultado.data,
            'message': 'Venta creada'
        })
        # al momento de crear el detalle validar si existe el plato

# modificar una nota de pedido para agregar mas productos


# TAREA!
# Devolver todas las mesas de un mozo,
# mandar el token del mozo y debera retornar todas sus mesas que ha atendido
# no importa si se repiten las mesas
# indicar el numero de mesa
# /mozo/mesas
# Al menos llegar a la creacion de la vista y mostrar el usuario de la token
class MostrarMesasMozoController(generics.ListAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = MostrarMesasMozoSerializer
    permission_classes = [IsAuthenticated, soloMozos]

    def get(self, request):
        print(request.user)
        resultado = self.serializer_class(instance=request.user)
        return Response({
            'success': True,
            'content': resultado.data
        })


class GenerarComprobantePagoController(generics.CreateAPIView):
    serializer_class = GenerarComprobanteSerializer
    queryset = CabeceraComandaModel.objects.all()

    def get_queryset(self, id):
        return self.queryset.filter(cabeceraId=id).first()

    def post(self, request, id_comanda):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid():
            pedido = self.get_queryset(id_comanda)

            return Response({
                'success': True
            })
        else:
            return Response({
                'success': False,
                'content': respuesta.errors
            })
