#Django Rest Framework
from rest_framework import serializers

#Models
from apps.perfilvehiculo.models import PerfilVehiculo

class PerfilVehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        models = PerfilVehiculo
        fiels = '__all__'
