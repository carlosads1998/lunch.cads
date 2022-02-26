from django.urls import path

from .models import item, pedido, entrega
from .views import itemAPIView, itensAPIView, pedidoAPIView, pedidosAPIView, entregaAPIView, entregasAPIView

urlpatterns = [
    path('item/', itemAPIView.as_view(), name='item'),
    path('item/<int:pk>/', itensAPIView.as_view(), name='itens'),
    path('pedido/', pedidoAPIView.as_view(), name='pedido'),
    path('pedido/<int:pk>/', pedidosAPIView.as_view, name='pedidos'),
    path('entrega/', entregaAPIView.as_view(), name='entrega'),
    path('entrega/<int:pk>/', entregasAPIView.as_view, name= 'entregas'),
]
