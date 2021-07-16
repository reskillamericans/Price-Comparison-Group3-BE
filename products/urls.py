
# Paths


from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('products/<pk>/deletecomment', views.deletecomment, name="deletecomment"),
    path('products/', views.products, name="products"),
    path('product_detail/<str:pk>/', views.product_detail, name="product_detail"),
    path('products/<pk>/add_comment', views.add_comment, name="add_comment"),
    path('products/<pk>/deletecomment', views.deletecomment, name="deletecomment"),
    path('products/<pk>/edit_comments', views.edit_comments, name="edit_comments"),
    
]