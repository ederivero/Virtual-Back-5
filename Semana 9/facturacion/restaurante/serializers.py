from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields = '__all__'


class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def save(self):
        personalCorreo = self.validated_data.get('personalCorreo')
        personalTipo = self.validated_data.get('personalTipo')
        personalNombre = self.validated_data.get('personalNombre')
        personalApellido = self.validated_data.get('personalApellido')
        password = self.validated_data.get('password')
        is_staff = False
        nuevoPersonal = PersonalModel(
            personalCorreo=personalCorreo,
            personalTipo=personalTipo,
            personalNombre=personalNombre,
            personalApellido=personalApellido,
            is_staff=is_staff
        )
        # encriptamos la contraseña
        nuevoPersonal.set_password(password)
        nuevoPersonal.save()
        return nuevoPersonal

    class Meta:
        model = PersonalModel
        # excluimos grupos porque no va a tener acceso al panel administrativo al igual que user_permissions (ambos sirven para indicar que puede hacer en el panel administrativo)
        exclude = ['groups', 'user_permissions']


class CustomPayloadSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomPayloadSerializer, cls).get_token(user)
        # ya tenemos la token que se suele devolver de manera automatica
        token['personalTipo'] = user.personalTipo
        token['otraCosa'] = 'valor secreto'
        print(token)
        return token


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaModel
        fields = '__all__'


class DetallePedidoCreacionSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(min_value=1)
    subtotal = serializers.DecimalField(max_digits=5, decimal_places=2)
    plato = serializers.IntegerField()


class NotaPedidoCreacionSerializer(serializers.Serializer):
    cliente = serializers.CharField(max_length=50, min_length=1)
    mesa = serializers.IntegerField()
    detalle = DetallePedidoCreacionSerializer(many=True)
