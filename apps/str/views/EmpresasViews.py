from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from apps.perfilempresa.models import PerfilEmpresa

#Serializers
from apps.str.serializers import perfilempresaserializers

@api_view(['GET'])
def ListadoEmpresas(request):
    obj = PerfilEmpresa.objects.all()
    elementos = []
    for i in obj:
        serializer = perfilempresaserializers.PerfilEmpresaSerializers(i)
        elementos.append(serializer.data)
    return Response(elementos)

@api_view(['GET'])
def DetallesEmpresas(request, slug):
    from django.shortcuts import get_object_or_404
    elementos = get_object_or_404(PerfilEmpresa, slug=slug)
    context = {
            'Modificado': elementos.modified,
            'Creado por': elementos.username.username,
            'ID': elementos.pk,
            'Compañia': elementos.nombre,
            'RNC': elementos.rnc,
            'Tipo de Combustible': elementos.tipocombustible,
            'Estatu': elementos.estatus,
    }
    return Response(context)

#POST
@api_view(['POST'])
def CreateEmpresa(request):
    serializer = perfilempresaserializers.CreateEmpresaSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    empresa = serializer.save()
    return Response(perfilempresaserializers.CreateEmpresaSerializers(empresa).data)
