#Django
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

#Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Models
from apps.perfilvehiculo.models import PerfilVehiculo

#Serializers
from apps.str.serializers import perfilvehiculoserializers

@api_view(['GET'])
def ListadoVehiculos(request):
    obj = PerfilVehiculo.objects.all()
    elementos = []
    for i in obj:
        serializer = perfilvehiculoserializers.PerfilVehiculoSerializers(i)
        elementos.append(serializer.data)
    return Response(elementos)

@api_view(['GET'])
def DetallesVehiculos(resquest, slug):
    from django.shortcuts import get_object_or_404
    obj = get_object_or_404(PerfilVehiculo, slug=slug)
    context = {
            'Fecha de Modificacion': obj.modified,
            'Registrado por': obj.registrado.username,
            'Empresa': obj.empresa.nombre,
            'Chasi': obj.chasis,
            'Matricula': obj.matricula,
            'Color Vehiculo': obj.color_vehiculo,
            'Remolque': obj.remolque,
            'Numero de Motor': obj.motor,
            'Numero de Solicitud': obj.solicitud,
            'Fecha en Servicio': obj.fecha_servicio,
    }
    return Response(context)


@api_view(['POST'])
def CreateVehiculos(request):
    serializers = perfilvehiculoserializers.CreateVehiculoSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    vehiculos = serializers.save()
    return Response(PerfilVehiculoSerializers.CreateVehiculoSerializers(vehiculos).data)
