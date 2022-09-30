from django import forms
from django.contrib import admin
#ESTO LOS QUE MUESTRA EN ADMIN PARA ADMINISTRAR EL DESDE EL SUPER USUARIO
from apps.clientes.models.cliente import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    
    list_display = [
        'nombres',
        'apellidos',
        'numero_identidad',
        'fecha_nacimiento',
        'ingreso_mensual',
    ]