from django.urls import path

from apps.clientes.views import CrearClienteViews
from apps.clientes.views import ClienteView
from apps.clientes.views.clientes import EditarClienteView, EliminaClienteView

app_name = 'clientes'
urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='cliente_list'),
    
    path('formulario/', CrearClienteViews.as_view(), name='formulario'),
    
    path('cliente/edit/<int:pk>/', EditarClienteView.as_view(), name='cliente_editar'),
    
    
    path('cliente/elimina/<int:pk>/', EliminaClienteView.as_view(), name='cliente_eliminar'),
    
    
    
]