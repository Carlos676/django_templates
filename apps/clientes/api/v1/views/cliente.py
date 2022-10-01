from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from apps.clientes.models import Cliente

from rest_framework import status

from apps.clientes.api.v1.serializers.clienteSerial import ClienteSerializer2

class ClienteView(ListAPIView):
    model= Cliente
    serializer_class = ClienteSerializer2
    queryset = Cliente.objects.all()
    
    def list(self, request, *arg, **kwargs):
        print("ingrsanado al metofo de aliex")
        clientes = Cliente.objects.all()
        cliente_serializer=ClienteSerializer2(clientes,many=True)
        print("Clientes Consulta\n",clientes)
        print("\nClientes Serializer\n",cliente_serializer)
        print("\nClientes Serializer\n",cliente_serializer.data)
        return self.get_paginated_response(self.paginate_queryset(cliente_serializer.data))
    
    def create(self, request, *args, **kwarga):
        #este metodo es para crear un registro nuevo de un cliente
        print("Creando un nuevo Cliente")
        return Response({"mje":"se a creado corectamente"})
    
    
    
    
    