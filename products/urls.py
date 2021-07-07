
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name="products"),
    path('new_comment', views.new_comment, name='new_comment'),
    path('edit_comment', views.edit_comment, name='edit_comment'),
    path('delete_comment', views.delete_comment, name='delete_comment'),


]