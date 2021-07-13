# Framework for Price Comparison tool

from django.db import models




class Product(models.Model):
    product_name = models.CharField(max_length=512, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    miscellaneous = models.CharField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        
        ordering = ['price']

    def __str__(self):
        return self.product_name


