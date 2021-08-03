# Framework for Price Comparison tool
from django.contrib.auth import get_user_model
from django.db import models

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


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    content = models.TextField(max_length=3000)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created']

    def __str__(self):
        return 'Comment on {} by {}'.format(self.product, self.user)
