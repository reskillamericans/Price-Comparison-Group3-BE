# Framework for Price Comparison tool

from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    miscellaneous = models.CharField(max_length=3000)
# Create Models

