from django.urls import path
from apps.clientes.api.v1.views.cliente import ClienteView

app_name = 'clientes'
urlpatterns = [
    path('lista-clientes/',
         ClienteView.as_view(),
         name="cliente-list"),
    
]
