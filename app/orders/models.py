from django.db import models

from app.products.models import Product
from app.users.models import User


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    count = models.PositiveIntegerField(default=1)
    price_at_purchase = models.IntegerField(null=True)

    @property
    def total_price(self):
        return self.price_at_purchase * self.count


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)

    order_items = models.ForeignKey(
        OrderItem,
        null=True,
        on_delete=models.PROTECT,
        related_name='orders',
    )

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='orders',
    )

    @property
    def total_price(self):
        for item in self.order_items:
            ...
