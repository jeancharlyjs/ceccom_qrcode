from django.contrib import admin
#Models
from apps.perfilempresa.models import PerfilEmpresa
from apps.perfilvehiculo.models import PerfilVehiculo

class PerfilEmpresalAdmin(admin.ModelAdmin):
    list_display = (
            'rnc',
            'nombre',
            'tipocombustible',
            'slug',
            'logopinture',
            'estatus',
    )
class PerfilVehiculoAdmin(admin.ModelAdmin):
    list_display = (
            'registrado',
            'url',
            'empresa',
            'marca',
            'chasi',
            'matricula',
            'slug',
            'color_vehiculo',
            'motor',
            'logopinture',
            'solicitud',
            'fecha_servicio',
            'remolque',
            'tipo_dimension',
            'tipocombustible',
            'capacidad',

    )
admin.site.register(PerfilEmpresa, PerfilEmpresalAdmin)
admin.site.register(PerfilVehiculo, PerfilVehiculoAdmin)
