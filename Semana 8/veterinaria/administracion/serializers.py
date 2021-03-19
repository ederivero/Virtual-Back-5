from rest_framework import serializers
from .models import EspecieModel


class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        # para que haga match con el model y pueda jalar las columnas con sus propiedades
        model = EspecieModel
        # indicar que columnas (atributos) quiero utilizar en este serializador
        # si queremos usar todos los campos => '__all__'
        # si queremos solamente usar ciertos campos (minoria) => ['campo1', 'campo2']
        fields = "__all__"
        # si queremos usar la mayora de campos y evitar una minoria => exclude = ['campos3', 'campo4']
        # NOTA: no se pueden usar los dos a la vez ya que genera ambiguedad
        # NOTA2: la unica forma de declara el exclude es mediante LIST, TUPLE ya que no admite el valor de __all__ si hacemos esto estariamos excluyendo todos los atributos del modelo
        # exclude = ('especieId',)
