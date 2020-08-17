from django.db import models


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    price = models.CharField(max_length=10)


class BasketItem(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )


