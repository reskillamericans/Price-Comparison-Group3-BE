# Framework for Price Comparison tool

from django.db import models
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint
from django.db.models import Count
from django.db.models.fields import AutoField
from django.forms import ModelForm



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


class Comments(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')
    content = models.TextField(max_length=3000, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['last_update']

    def __str__(self):
        return self.content


