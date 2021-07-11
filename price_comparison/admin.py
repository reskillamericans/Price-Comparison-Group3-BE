# Model Registry

from django.contrib import admin
from .models import Product, Comments


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('product_name', 'price', 'description', 'miscellaneous', 'created_at', 'updated_at')
    list_filter = ('product_name', 'price', 'created_at')
    search_fields = ('product_name', 'price', 'created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    model = Comments
    list_display = ('product', 'user', 'last_update')
    list_filter = ('product', 'last_update')
    search_fields = ('user', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Comments, CommentAdmin)

# Register your models here.
