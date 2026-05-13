from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from app.orders.models import Order
from app.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
