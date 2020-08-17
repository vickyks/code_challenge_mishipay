from django.db import models


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    price = models.CharField(max_length=10)


class ProductVariant(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    product =  models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)


class BasketItem(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )


class InventoryItem(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    sku = models.CharField(max_length=20)

    cost = models.
    country_code_of_origin
    created_at
    harmonized_system_code

