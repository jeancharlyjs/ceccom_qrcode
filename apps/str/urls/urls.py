#Django
from django.urls import path
from apps.str.views import (EmpresasViews,
                            VehiculosViews)

app_name = 'apps'

urlpatterns = [
    path('empresas/', EmpresasViews.Listado, name='listadoempresa'),
    path('empresas/detalles/<slug:slug>/', EmpresasViews.DetallesEmpresas, name='detalles'),
    path('vehiculos/', VehiculosViews.Listado, name='listadoVehiculo'),
    path('vehiculos/detalles/<slug:slug>/', VehiculosViews.DetallesVehiculos, name='vdetalles'),
]
