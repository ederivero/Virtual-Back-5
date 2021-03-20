from .models import ClienteModel, EspecieModel, RazaModel, MascotaModel
from .serializers import EspecieSerializer, RazaEscrituraSerializer, RazaVistaSerializer, MascotaSerializer
# las vistas genericas sirven para ya no hacer mucho codigo pero no estamos estandarizando las respuestas de nuestra api (si da un error lanzara un status 500 sin ningun mensaje), si hay info retornara una lista o un objeto, si no mandamos la data correctamente solamente nos mostrara el mensaje de error
# Obviamente estas vistas genericas se pueden modificar y se pueden alterar segun nuestros requerimientos
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# sirve para devolver una Respuesta mejor elaborada al usuario
from rest_framework.response import Response
from rest_framework import status
# Asi se importa si vas a usar una class APIView
from rest_framework.views import APIView
# Asi si vas a usar un decorator
# https://www.django-rest-framework.org/api-guide/views/#api-policy-decorators
from rest_framework.decorators import api_view

from django.db.models import Count
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
    serializer_class = RazaEscrituraSerializer

    def post(self, request):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid() is True:
            print(respuesta.validated_data)
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
        respuesta = RazaVistaSerializer(
            instance=self.filtrar_razas(), many=True)
        # print(self.get_queryset()[1].especie)
        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })


class MascotasController(ListCreateAPIView):
    queryset = MascotaModel.objects.all()
    serializer_class = MascotaSerializer

    def post(self, request):
        resultado = self.serializer_class(data=request.data)
        if resultado.is_valid():
            resultado.save()
            return Response({
                "success": True,
                "content": resultado.data,
                "message": "Mascota registrada exitosamente"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "content": resultado.errors,
                "message": "Hubo un error al registrar la mascota"
            }, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        resultado = self.serializer_class(
            instance=self.get_queryset(), many=True)
        return Response({
            "success": True,
            "content": resultado.data,
            "message": None
        })


# Luego de usar las vistas genericas podemos tambien utilizar algunas vistas con total control de nuestro metodos, se puede realizar en forma de una clase o en forma de una funcion
# al usar APIViews no tenemos que indicar a que modelo corresponde ni a que serializador van a cumplir ordenes ya que en cada metodo podemos acceder a diferentes modelos
class CustomController(APIView):
    # el api view se puede utilizar para trabajar con varios modelos dentro de la misma clase
    # https://www.django-rest-framework.org/api-guide/views/

    def get(self, request):
        return Response({
            "message": "Esto es un controlador de prueba"
        })

    def post(self, request):
        pass


# Tambien se puede crear ApiViews sin la necesidad de hacerlo mediante una clase, se usaria un decorador
@api_view(['GET', 'POST'])
def prueba(request):  # /usuario/:id
    print(request.method)
    print(request.data)
    if(request.method == 'POST'):
        pass
    return Response({
        "message": "Esto es un controlador de prueba!"
    })


# hacer un controlador para contabilizar la cantidad de perros nacidos en determinado año
# SELECT * FROM t_mascota where mascota_fecnac BETWEEN "2018-01-01" and "2018-12-31";
# En el ORM seria => MascotaModel.objects.filter(mascotaFechaNacimiento__range=("2018-01-01","2018-12-31"))
class BusquedaController(ListAPIView):
    queryset = MascotaModel.objects.all()
    serializer_class = MascotaSerializer

    def get(self, request):
        # print(request.query_params.get('raza'))
        if request.query_params.get('fecha'):
            anio = request.query_params.get('fecha')
            # mascotas = MascotaModel.objects.filter(
            # mascotaFechaNacimiento__range=(anio+"-01-01", anio+"-12-31")).all()
            # Para ver todas las combinaciones posibles entre las columnas y sus opciones => https://docs.djangoproject.com/en/3.1/ref/models/querysets/#gt
            # SELECT * FROM t_mascota where YEAR(mascota_fecnac) = 2018;
            mascotas = MascotaModel.objects.filter(
                mascotaFechaNacimiento__year=anio).all()
            resultado = self.serializer_class(mascotas, many=True)
            return Response({
                "success": True,
                "content": resultado.data,
                "message": None
            })
        else:
            return Response({
                "success": False,
                "content": None,
                "message": "No de proveyeron los campos suficientes"
            })


# controlador para contabilizar cuantas mascotas son machos y cuantas mascotas son hembras
@api_view(['GET'])
def contabilitar_sexo(request):
    # Seleccionar que values vamos a utilizar para esta consulta
    # el metodo values sirve para indicar que columnas vamos a utilizar de la tabla
    # Luego el count sirve para hacer la cuenta de en este caso las mascotaSexo
    # el annotate sirve para hacer clausulas de agrupamiento
    # Order by es una clausula de ordenamiento en el cual su valor por defecto es ASCENDENTE, si queremos ordenar de manera descendente simplemente ponemos un '-' antes de la columna
    resultado = MascotaModel.objects.values(
        'mascotaSexo').annotate(Count('mascotaSexo')).order_by('mascotaSexo')
    # Si queremos hacer un ordeamiento usando alguna relacion con una columna de un padre
    pruebas = MascotaModel.objects.order_by('-raza__razaNombre').all()
    # Busqueda de todas las mascotas cuando su razanombre sea Dobberman
    # select * from t_mascota
    # join t_raza on t_mascota.raza_id = t_raza.raza_id
    # join t_especie on t_raza.especie_id = t_especie.especie_id
    # where especie_nombre ="Perrito" ;
    pruebas = MascotaModel.objects.filter(
        raza__especie__especieNombre="Perrito").all()
    # devolviendo todas las especies cuyo mascota_nombre = "Mocha", entonces para ingresar a la mascota usamos el related_name entre especie y raza "especiesRaza" luego ingresamos a la entidad Mascota mediante su related_name "mascotasRaza" y recien ahi estaremos en la entidad Mascota y podremos usar todos sus atributos como mascotaNombre
    pruebas = EspecieModel.objects.filter(
        especiesRaza__mascotasRaza__mascotaNombre="Mocha").all()
    # Nota: el accesso entre entidades no solamente se hace en el filter, se puede ocupar en cualquiera de los metodos del objects, por ejemplo: filter() order_by() annotate() values(), etc..
    print(pruebas)
    # print(resultado)
    # para mas informacion sobre como hacer clausulas LIKE, ordenamiento, agrupamiento, ingresar a los padres, a los hijos, etc:
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets
    return Response({
        "success": True,
        "content": resultado
    })
