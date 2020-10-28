#Django Rest Framework
from rest_framework import serializers

#Models
from apps.perfilvehiculo.models import PerfilVehiculo

#Utilidades
# from django.utils.translation import ugettext_lazy as _

class PerfilVehiculoSerializers(serializers.Serializer):
    registrado = serializers.CharField()
    empresa = serializers.CharField()
    marca = serializers.CharField()
    chasis = serializers.CharField()
    matricula = serializers.CharField()
    slug = serializers.SlugField()
    color_vehiculo = serializers.CharField()
    motor = serializers.CharField()
    solicitud = serializers.CharField()
    fecha_servicio = serializers.DateTimeField()
    remolque = serializers.CharField()

class CreateVehiculoSerializers(serializers.Serializer):


    def create(self, datos):
        return PerfilVehiculo.objects.create(**data)
