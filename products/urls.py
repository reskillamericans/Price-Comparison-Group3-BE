
# Paths


from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/edit_comments/<int:id>/', views.edit_comments, name="edit_comments"),
    path('<int:pk>/deletecomment/<int:id>/', views.deletecomment, name="deletecomment"),
    path('products/', views.products, name="products"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/<int:pk>/add_comment', views.add_comment, name="add_comment"),
    
    
]