from django.http import response
from .models import EspecieModel
from .serializers import EspecieSerializer
# las vistas genericas sirven para ya no hacer mucho codigo pero no estamos estandarizando las respuestas de nuestra api (si da un error lanzara un status 500 sin ningun mensaje), si hay info retornara una lista o un objeto, si no mandamos la data correctamente solamente nos mostrara el mensaje de error
# Obviamente estas vistas genericas se pueden modificar y se pueden alterar segun nuestros requerimientos
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# sirve para devolver una Respuesta mejor elaborada al usuario
from rest_framework.response import Response
from rest_framework import status

# Las APIViews sirven para darnos ya los metodos que pueden ser accedidos a esta clase, en el siguiente caso sera el metedo GET, POST
# pero adicional a ello queremos implementar un metodo mas se puede realizar con total normalidad y no vamos a tener ningun problema


class EspeciesController(ListCreateAPIView):
    # queryset es la consulta que se realizará a la bd en todo el controlador
    queryset = EspecieModel.objects.all()  # SELECT * FROM t_especie
    serializer_class = EspecieSerializer

    # lo unico que se puede responder al Client es un diccionario, una lista o un string | integer
    # todo lo que concierne al parametro request => https://www.django-rest-framework.org/api-guide/requests/
    # el metodo get_queryset sirve para devolvernos la data actual en la base de datos, si llamamos al atributo self.queryset lo se hara sera devolver toda la data que teniamos al momento de levantar el proyecto
    # def get_queryset(self):
    #     return self.queryset.all()

    def get(self, request):
        # en el request se almacenan todos los datos que me manda el front (headers, body, cookies, etc)
        # print(self.queryset)
        respuesta = self.serializer_class(
            instance=self.get_queryset(), many=True)
        # la data es la informacion ya serializada que puede ser enviada al front
        print(respuesta.data)
        return Response(data={
            "success": True,
            "content": respuesta.data,
            "message": None
        }, status=200)

    def post(self, request):
        # la forma para capturar lo que me esta mandando el client es mediante el request
        # request.data
        self.serializer_class()
        data = self.serializer_class(data=request.data)
        # el metodo is_valid() se encarga de validar si la data que se da es la indica para usarse en el modelo
        # NOTA: solo se puede usar ese metodo cuando le pasamos el parametro data
        # si indicamos el parametro raise_exception = True este detendra el procedimiento habilital y para todo para responder los errores que esten en el serializer
        # print(data.is_valid())
        # si queremos manejar los errores tendremos que usar el atribot errors del serializer y ahi nos detallara todos los errores del porque la data no es valida
        # el atributo errors se generara después de haber llamado al metodo is_valid() y si su resultado es false
        # print(data.errors)
        if (data.is_valid()):
            # serializer_class al ser un serializador de tipo SerializerModel ya trae un metodo predeterminado llamado save() el cual se encarga de guardar el nuevo registro en la bd
            data.save()
            # si queremos la data de ese nuevo registro usaremos su atributo .data que nos devolvera un diciconario con la nueva informacion guardada en la bd
            return Response(data={
                "success": True,
                "content": data.data,
                "message": None
            }, status=201)
        else:
            print(data.errors.get("especieNombre")[0])
            texto = "{} ya se encuentra registrado!".format(
                request.data.get("especieNombre"))
            data.errors.get("especieNombre")[0] = texto
            return Response(data={
                "success": False,
                "content": data.errors,
                "message": "Hubo un error al guardar la especie"
            }, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     print("hizo put")
    #     return Response("ok")


class EspecieController(RetrieveUpdateDestroyAPIView):
    queryset = EspecieModel.objects.all()
    serializer_class = EspecieSerializer

    def get_queryset(self, id):
        return EspecieModel.objects.filter(especieId=id).first()

    def get(self, request, id):
        especie = self.get_queryset(id)
        print(type(especie))
        respuesta = self.serializer_class(instance=especie)
        # indicar si el resultado de la busqueda es vacio mostrar un mensaje de not found con su estado correspondiente
        if respuesta.data is not None:
            print("no esta vacio")
        return Response(data={
            "success": True,
            "content": respuesta.data,
            "message": None
        })

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass
