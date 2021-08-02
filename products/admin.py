from django.contrib import admin

from .models import Product, LikeButton

admin.site.register(Product)
admin.site.register(LikeButton)
