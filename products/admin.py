from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['product_name', 'image', 'price', 'description', 'miscellaneous','created_at', 'updated_at']
    list_filter = ['product_name', 'price', 'updated_at']
    search_fields = ['product_name', 'price', 'description']
    


admin.site.register(Product, ProductAdmin)


