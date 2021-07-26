from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [

    path('<int:pk>/edit_comments/<int:id>/', views.edit_comments, name="edit_comments"),
    path('<int:pk>/deletecomment/<int:id>/', views.deletecomment, name="deletecomment"),
    path('products/', views.products, name="products"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/<int:pk>/add_comment', views.add_comment, name="add_comment"),
    # path('index', views.index, name='index'),
    # Products
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # Likes
    path('like/', views.like_button, name='like'),

    # Add and Delete Product
    path('add_products/', views.add_product_view, name='add_products'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    ]

