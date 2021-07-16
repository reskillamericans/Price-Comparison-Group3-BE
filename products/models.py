# Framework for Price Comparison tool

from django.contrib.auth.models import User
from django.db import models
from accounts.models import User



class Product(models.Model):
    product_name = models.CharField(max_length=512, blank=True, null=True)
    image = models.URLField(blank=None, default=True)
    amazon_price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    ebay_price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    description = models.TextField(blank=True, null=True)
    miscellaneous = models.CharField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def number_of_comments(self):
        return Comments.objects.filter(product_connected=self).count()
    

    def __str__(self):
        return self.product_name

class Comments(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    content = models.TextField(max_length=3000, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(user):
        user.approved_comment = True
        user.save()

    def approved_comments(self):
        return self.content.filter(approved_comment=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['last_update']

    def __str__(self):
        return 'Comment on {} by {}'.format(self.product, self.user)