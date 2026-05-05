from django.db import models

from app.products.models import Product
from app.users.models import User


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)

    products = models.ManyToManyField(
        Product,
        through='OrderItem',
        related_name='orders',
    )

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='orders',
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    count = models.PositiveIntegerField(default=1)
    price_at_purchase = models.IntegerField()
