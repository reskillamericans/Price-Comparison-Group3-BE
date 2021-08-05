from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # path('index', views.index, name='index'),
    # Products
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('modal/<int:pk>/', views.ProductModalView.as_view(), name='product_modal'),

    # Comments
    path('add_comment/<int:product_id>', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),

    path('product_comments/<int:pk>', views.ProductComments.as_view(), name='product_comments'),

    # Likes
    path('like/', views.like_button, name='like'),

    # Add and Delete Product
    path('add_product/', views.add_product_view, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    ]
