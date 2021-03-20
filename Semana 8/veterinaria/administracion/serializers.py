from rest_framework import serializers
from .models import EspecieModel, RazaModel


class MostrarRazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RazaModel
        fields = '__all__'


class EspecieSerializer(serializers.ModelSerializer):
    # este es el funcionamiento base del metodo save del serializer
    # def save(self):
    #     especie = EspecieModel(especieNombre = self.validated_data.especieNombre)
    #     especie.save()
    #     self.instance = especie
    #     return especie
    razas = MostrarRazaSerializer(
        source="especiesRaza", many=True, read_only=True)

    def update(self):
        # el atributo instance es la instancia de la clase y me da acceso a todos los atributos de la clase
        print(self.instance)
        # es la data mandada por el front PERO que ya paso un filtro de validacion (que cumple con las condiciones definidas por el modelo) y se genera cuando se llama al metodo is_valid()
        print(self.validated_data)
        self.instance.especieNombre = self.validated_data.get("especieNombre")
        self.instance.especieEstado = self.validated_data.get("especieEstado")
        # el metodo save() es el metodo de los MODELOS que se encarga de hacer el guardado en la bd
        self.instance.save()
        # el atributo data es el encargo de maquillar la informacion para que el front la pueda visualizar sin problemas
        return self.data

    def delete(self):
        # Forma 1
        # self.instance.especieEstado = False
        # self.instance.save()
        # return self.instance
        # Forma 2
        if(self.instance):
            self.instance.especieEstado = False
            self.instance.save()
            return self.instance
        return None

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


class EspecieVistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EspecieModel
        exclude = ['especieEstado']


class RazaEscrituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RazaModel
        fields = '__all__'


class RazaVistaSerializer(serializers.ModelSerializer):
    especie = EspecieVistaSerializer()

    class Meta:
        model = RazaModel
        fields = '__all__'
