from .models import EspecieModel, RazaModel
from .serializers import EspecieSerializer, RazaSerializer
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
        # print(respuesta.data)
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
            # print(data.errors.get("especieNombre")[0])
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
        print(especie.especiesRaza.all())
        respuesta = self.serializer_class(instance=especie)
        # indicar, si el resultado de la busqueda es vacio mostrar un mensaje de not found con su estado correspondiente
        # el instance dara la instancia si es que tiene una y sino dara None (vacio)
        # print(respuesta.instance)
        # FORMA 1:
        # respuesta.data.get("especieId")
        # FORMA 2:
        # respuesta.instance
        # FORMA 3:
        if especie:
            return Response(data={
                "success": True,
                "content": respuesta.data,
                "message": None
            })
        else:
            return Response(data={
                "success": True,
                "content": None,
                "message": "No se encontro la especie con ID {}".format(id,)
            })

    def put(self, request, id):
        especie = self.get_queryset(id)
        respuesta = self.serializer_class(instance=especie, data=request.data)
        if respuesta.is_valid():
            return Response(data={
                "success": True,
                "content": respuesta.update(),
                "message": "Se actualizo la especie exitosamente"
            })
        else:
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # 1. Agregar una columna en la tabla especie que sea "especieEstado" que sea boolean y que x defecto sea true y no puede ser vacio ✔
        # 2. Modificar el metodo update para que admita el estado ✔
        # 3. al momento de hacer delete NO ELIMINAR la especie sino cambiar su estado a False (inhabilitado) ✔
        # 4. Indicar al usuario que se inhabilito correctamente la especie ✔
        # NOTA: hacer la eliminacion en el serializer (crear un metodo para ello)
        # screenshot de la tabla especie
        # screenshot del serializer (del metodo)
        # screenshot del metodo delete
        # Practica # 2
        # si el id es incorrecto no pasar a la fase de "eliminacion"
        # hay dos formas: 1. hacerlo en el controller como el update y la 2. es hacerlo en el metodo delete
        # solucion 1
        # especie = self.get_queryset(id)
        # if especie:
        #     respuesta = self.serializer_class(instance=especie)
        #     respuesta.delete()
        #     return Response(data={
        #         "success": True,
        #         "content": None,
        #         "message": "se inhabilito la especie exitosamente"
        #     })
        # else:
        #     return Response(data={
        #         "success": False,
        #         "content": None,
        #         "message": "Especie no existe"
        #     })
        # solucion 2
        respuesta = self.serializer_class(instance=self.get_queryset(id))
        if respuesta.delete():
            return Response(data={
                "success": True,
                "content": None,
                "message": "se inhabilito la especie exitosamente"
            })
        else:
            return Response(data={
                "success": False,
                "content": None,
                "message": "Especie no existe"
            })


class RazasController(ListCreateAPIView):
    queryset = RazaModel.objects.all()
    serializer_class = RazaSerializer

    def post(self, request):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid() is True:
            respuesta.save()
            return Response(data={
                "success": True,
                "content": respuesta.data,
                "message": "Raza creada exitosamente"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            }, status=status.HTTP_400_BAD_REQUEST)

    def filtrar_razas(self):
        """Metodo que sirve para filtrar las razas en la base de datos y devuelve solamente las razas cuya especie esten habilitadas (true)"""
        razas = RazaModel.objects.all()
        resultado = []
        for raza in razas:
            if (raza.especie.especieEstado is True):
                resultado.append(raza)
        return resultado

    def get(self, request):
        # solamente me muestre las razas con especies habilitadas
        respuesta = self.serializer_class(
            instance=self.filtrar_razas(), many=True)
        # print(self.get_queryset()[1].especie)
        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })
