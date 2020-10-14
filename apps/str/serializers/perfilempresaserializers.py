#Django Rest Framework
from rest_framework import serializers

from apps.perfilempresa.models import PerfilEmpresa

class PerfilEmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PerfilEmpresa
        fiels = "__all__"
