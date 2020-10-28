#Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Django
from django.contrib.auth.models import User
#Models
from apps.perfilempresa.models import PerfilEmpresa

class PerfilEmpresaSerializers(serializers.Serializer):
    username = serializers.CharField()
    rnc = serializers.CharField()
    nombre = serializers.CharField()
    direccion = serializers.CharField()
    tipocombustible = serializers.CharField()
    slug = serializers.SlugField()
    estatus = serializers.CharField()

class CreateEmpresaSerializers(serializers.Serializer):

    # username = serializers.CharField(
    #     max_length=150,
    #     allow_blank=False,
    # )
    rnc = serializers.RegexField("[0-9]{11}")
    nombre = serializers.CharField()
    direccion = serializers.CharField(
        max_length=150,
        allow_blank=False,
    )
    TIPO_COMBUSTIBLE = (
            ('G', 'Gas'),
            ('GN', 'Gas Natural'),
            ('GSL', 'Gasoil'),
            ('GS', 'Gasolina'),
)
    tipocombustible = serializers.ChoiceField(
        choices=TIPO_COMBUSTIBLE,
    )
    # slug = serializers.SlugField(
    #     max_length=50,
    #     validators=[
    #         UniqueValidator(queryset=PerfilEmpresa.objects.all())
    #     ]
    # )
    # logopinture = serializers.ImageField(
    #     max_length=None,
    #     allow_empty_file=False,
    #     )
    STATUS = (
            ('N', "Normalizado"),
            ('I', "Investigacion"),
            ('C', "Clausurada"),
    )
    estatus = serializers.ChoiceField(
        choices=STATUS,
    )
    def create(self, data):
        return PerfilEmpresa.objects.create(**data)
