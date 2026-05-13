from django.db import models
from django.db.models import F, Sum

from app.products.models import Product
from app.users.models import User


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='orders',
    )

    @property
    def total_price(self):
        return self.items.aggregate(
            total=Sum(F('price_at_purchase') * F('count'))
        )['total'] or 0


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    count = models.PositiveIntegerField(default=1)
    price_at_purchase = models.IntegerField()

    order = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
        related_name='items',
    )

    @property
    def total_price(self):
        return self.price_at_purchase * self.count
