from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from apps.perfilempresa.models import PerfilEmpresa

@api_view(['GET'])
def Listado(request):
    obj = PerfilEmpresa.objects.all()
    elementos = []
    for i in obj:
        elementos.append({
            'Usuario': i.username.username,
            'Nombre': i.nombre,
            'URL': "localhost:8000/detalles/"+i.slug+"/",
        })
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
