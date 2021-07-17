
# Paths


from django.urls import path

from . import views

urlpatterns = [
    
    path('products/<int:pk>/deletecomment', views.deletecomment, name="deletecomment"),
    path('products/', views.products, name="products"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/<int:pk>/add_comment', views.add_comment, name="add_comment"),
    path('products/<pk>/edit_comments', views.edit_comments, name="edit_comments"),
    
]