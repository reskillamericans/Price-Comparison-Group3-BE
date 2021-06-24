# Model Registry

from django.contrib import admin
from .models import Price, Description, ProductName, AdditionalInfo

admin.site.register(Price)
admin.site.register(Description)
admin.site.register(ProductName)
admin.site.register(AdditionalInfo)


# Register your models here.
