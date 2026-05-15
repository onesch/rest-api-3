from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from app.orders.models import Order
from app.orders.serializers import OrderSerializer, GetUserOrdersSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"])
    def get_user_orders_by_date(self, request):

        # validate input data
        serializer = GetUserOrdersSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # business logic
        user_id = serializer.validated_data["user_id"]
        date_start = serializer.validated_data["date_start"]
        date_finish = serializer.validated_data["date_finish"]

        orders = Order.objects.filter(
            user=user_id,
            date__range=(date_start, date_finish),
        )

        return Response(
            OrderSerializer(orders, many=True).data
        )
