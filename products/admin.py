from django.contrib import admin
from .models import Product, Comments


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('product_name', 'price', 'image', 'description', 'created_at', 'miscellaneous', 'updated_at')
    list_filter = ['product_name', 'price', 'updated_at']
    search_fields = ['product_name', 'price', 'description']


class CommentAdmin(admin.ModelAdmin):
    model = Comments
    list_display = ('product', 'user', 'content', 'last_update')
    list_filter = ['product', 'user', 'last_update']
    search_fields = ['product', 'user', 'content']


admin.site.register(Product, ProductAdmin)
admin.site.register(Comments, CommentAdmin)

