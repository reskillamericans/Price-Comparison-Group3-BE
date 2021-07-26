# Framework for Price Comparison tool
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()


class Product(models.Model):
    product_name = models.CharField(max_length=512, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    amazon_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ebay_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amazon_url = models.URLField(blank=True, null=True, default=None)
    ebay_url = models.URLField(blank=True, null=True, default=None)
    amazon_asin = models.CharField(max_length=12, blank=True, null=True, default=None)
    category = models.CharField(max_length=200, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    miscellaneous = models.CharField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class LikeButton(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True, related_name='likebutton')

    # content = models.TextField(null=True)

    def __str__(self):
        return f"{self.product.product_name} Likes"

    @property
    def total_likes(self):
        return self.user.count()
