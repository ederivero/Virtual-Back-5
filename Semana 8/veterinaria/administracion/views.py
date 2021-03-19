from .models import EspecieModel
from .serializers import EspecieSerializer
# las vistas genericas sirven para ya no hacer mucho codigo pero no estamos estandarizando las respuestas de nuestra api (si da un error lanzara un status 500 sin ningun mensaje), si hay info retornara una lista o un objeto, si no mandamos la data correctamente solamente nos mostrara el mensaje de error
# Obviamente estas vistas genericas se pueden modificar y se pueden alterar segun nuestros requerimientos
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

# sirve para devolver una Respuesta mejor elaborada al usuario
from rest_framework.response import Response


# Las APIViews sirven para darnos ya los metodos que pueden ser accedidos a esta clase, en el siguiente caso sera el metedo GET, POST
# pero adicional a ello queremos implementar un metodo mas se puede realizar con total normalidad y no vamos a tener ningun problema
class EspeciesController(ListCreateAPIView):
    # queryset es la consulta que se realizará a la bd en todo el controlador
    queryset = EspecieModel.objects.all()  # SELECT * FROM t_especie
    serializer_class = EspecieSerializer

    # lo unico que se puede responder al Client es un diccionario, una lista o un string | integer
    # todo lo que concierne al parametro request => https://www.django-rest-framework.org/api-guide/requests/
    def get(self, request):
        # en el request se almacenan todos los datos que me manda el front (headers, body, cookies, etc)
        print(self.queryset)
        return Response(data={
            "success": True,
            "content": None,
            "message": None
        }, status=200)

    def post(self, request):
        print("hizo post")
        return Response(data={
            "success": True,
            "content": None,
            "message": None
        }, status=200)

    # def put(self, request):
    #     print("hizo put")
    #     return Response("ok")
