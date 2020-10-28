#Django
from django.urls import path
from apps.str.views import (EmpresasViews,
                            VehiculosViews,
                            SessionViews,)

app_name = 'apps'

urlpatterns = [
    path('empresas/', EmpresasViews.ListadoEmpresas, name='listadoempresa'),
    path('empresas/create/', EmpresasViews.CreateEmpresa, name='cretaempresa'),
    path('empresas/detalles/<slug:slug>/', EmpresasViews.DetallesEmpresas, name='detalles'),
    path('vehiculos/', VehiculosViews.ListadoVehiculos, name='listadoVehiculo'),
    path('vehiculos/detalles/<slug:slug>/', VehiculosViews.DetallesVehiculos, name='vdetalles'),

    #PATH SESSION
    path('session/', SessionViews.listado, name='session'),
]
