
from django.urls import path

from . import views


urlpatterns = [
    path('base/', views.base, name="base"),
    path('products/products/', views.products, name="products"),
    path('viewcomments/', views.viewcomments, name="viewcomments"),
    path('addcomments/', views.addcomments, name="addcomments"),
    path('retrieveproduct/<int:pk>/', views.retrieveproduct, name="retrieveproduct"),
    path('edit_comment/', views.edit_comment, name="edit_comment"),
    path('delete_comment/', views.delete_comment, name="delete_comment"),


]