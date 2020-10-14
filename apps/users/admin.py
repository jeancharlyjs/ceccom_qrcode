from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import UserPerfil
from apps.perfil.models import PerfilCliente, Referencia, PerfilLaboral
from apps.pretamos.models import PretamosCliente
from apps.desembolso.models import Desembolso

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'created',
        'modified',
    )
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        # 'cedula_id',
        'usuario',
        'created',
        'first_name',
        'last_name',
        'sexo',
        'EstdoCivil',
    )
    prepopulated_fields = {
        'slug': ('cedula_id',)
    }
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class LaboralAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class PretamosClienteAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class DesembolsoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
admin.site.register(Desembolso, DesembolsoAdmin)
admin.site.register(PretamosCliente, PretamosClienteAdmin)
admin.site.register(PerfilCliente, PerfilAdmin)
admin.site.register(Referencia, ReferenciaAdmin)
admin.site.register(PerfilLaboral, LaboralAdmin)
admin.site.register(UserPerfil, UserAdmin)
