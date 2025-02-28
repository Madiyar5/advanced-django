from django.db import models
from users.models import CustomUser
from products.models import Product


class Order(models.Model):
    ORDER_TYPES = (('buy', 'Buy'), ('sell', 'Sell'))

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)