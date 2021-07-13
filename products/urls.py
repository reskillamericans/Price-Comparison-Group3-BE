
from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name="products"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),



]