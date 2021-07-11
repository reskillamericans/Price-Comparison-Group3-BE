# Framework for Price Comparison tool

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=512, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    miscellaneous = models.CharField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Comments(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=3000, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_update']
        verbose_name_plural = "Comments"

    def __str__(self):
        return 'Comment {} by {}'.format(self.product, self.user)

