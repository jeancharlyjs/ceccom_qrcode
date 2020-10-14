#Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from apps.perfilvehiculo.models import PerfilVehiculo

@api_view(['GET'])
def Listado(request):
    obj = PerfilVehiculo.objects.all()
    elementos = []
    for i in obj:
        elementos.append({
            'Registrado por': i.registrado.username,
            'Empresa': i.empresa.nombre,
            'Chasi': i.chasi,
            'Matricula': i.matricula,
            'Color Vehiculo': i.color_vehiculo,
            'Numero de Motor': i.motor,
            'Numero de Solicitud': i.solicitud,
            'Fecha en Servicio': i.fecha_servicio,
            'Slug': i.slug,
        })
    return Response(elementos)

@api_view(['GET'])
def DetallesVehiculos(resquest, slug):
    from django.shortcuts import get_object_or_404
    obj = get_object_or_404(PerfilVehiculo, slug=slug)
    context = {
            'Fecha de Modificacion': obj.modified,
            'Registrado por': obj.registrado.username,
            'Empresa': obj.empresa.nombre,
            'Chasi': obj.chasi,
            'Matricula': obj.matricula,
            'Color Vehiculo': obj.color_vehiculo,
            'Remolque': obj.remolque,
            'Numero de Motor': obj.motor,
            'Numero de Solicitud': obj.solicitud,
            'Fecha en Servicio': obj.fecha_servicio,
    }
    return Response(context)
