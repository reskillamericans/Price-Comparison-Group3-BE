from django.contrib import admin
from .models import Product, Comments


class CommentAdmin(admin.ModelAdmin):
    model = Comments
    list_display = ['product', 'content', 'user', 'last_update']
    list_filter = ['product', 'user', 'last_update']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['product_name','pk', 'image', 'price', 'description', 'miscellaneous','created_at', 'updated_at',  ]
    list_filter = ['product_name', 'price', 'updated_at']
    search_fields = ['product_name', 'price', 'description']


admin.site.register(Comments, CommentAdmin)
admin.site.register(Product, ProductAdmin)


