from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('index', views.index, name='index'),
    # Products
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # Likes
    path('like/', views.like_button, name='like'),

    # Add and Delete Product
    path('add_products/', views.add_product_view, name='add_products'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    ]
