from django.db import models


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=150)
    inventory_level = models.IntegerField(null=True)


class InventoryItem(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    sku = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey(Order, related_name="line_items", on_delete=models.CASCADE)
