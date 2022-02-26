from dataclasses import fields
from .models import item, pedido, entrega
from rest_framework import serializers

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=item
        fields=(
            'id',
            'nomei',
            'descricao',
            'valor',
            'imagem',
        )

class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=pedido
        fields=(
            'id',
            'cliente',
            'ped_cliente',
            'quan',
            'pag',
        )

class entregaSerializer(serializers.ModelSerializer):
    class Meta:
        model=entrega
        fields=(
            'id',
            'identi',
            'status',
        )