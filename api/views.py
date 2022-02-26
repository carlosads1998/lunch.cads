from django.shortcuts import render
from .serializers import itemSerializer, pedidoSerializer, entregaSerializer
from .models import item, pedido, entrega
from rest_framework import generics

class itemAPIView(generics.ListCreateAPIView):
    queryset=item.objects.all()
    serializer_class=itemSerializer

class itensAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=item.objects.all()
    serializer_class=itemSerializer

class pedidoAPIView(generics.ListCreateAPIView):
    queryset=pedido.objects.all()
    serializer_class=pedidoSerializer

class pedidosAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=pedido.objects.all()
    serializer_class=pedidoSerializer

class entregaAPIView(generics.ListCreateAPIView):
    queryset=entrega.objects.all()
    serializer_class=entregaSerializer

class entregasAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=entrega.objects.all()
    serializer_class=entregaSerializer
