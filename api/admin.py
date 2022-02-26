from telnetlib import STATUS
from django.contrib import admin
from .models import item, pedido, entrega

@admin.register(item)
class itemAdmin(admin.ModelAdmin):
    list_display=('nomei','descricao', 'valor', 'imagem')
    
@admin.register(pedido)
class pedidoAdmin(admin.ModelAdmin):
    list_display=('cliente', 'ped_cliente', 'quan', 'pag')

@admin.register(entrega)
class entregaAdmin(admin.ModelAdmin):
    list_display=('identi', 'status')