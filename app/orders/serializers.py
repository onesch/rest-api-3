from rest_framework import serializers

from app.orders.models import Order, OrderItem
from app.products.models import Product
from app.users.models import User


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Product.objects.all(),
        source='product',
    )

    class Meta:
        model = OrderItem
        fields = [
            "product_name", "count", "price_at_purchase",
        ]
        read_only_fields = [
            "price_at_purchase",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user_email = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all(),
        source='user',
    )

    class Meta:
        model = Order
        fields = [
            "user_email", "items", "total_price",
        ]

    def create(self, validated_data: dict):
        items_data = validated_data.pop('items')

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            product = item_data['product']
        
            OrderItem.objects.create(
                order=order,
                product=product,
                count=item_data['count'],
                price_at_purchase=product.price,
            )

        return order
