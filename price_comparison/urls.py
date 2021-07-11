
# Paths

from . import views
from django.urls import path

urlpatterns = [
    # path('', views.new_comment, name="new_comment"),
    path('<slug:slug>/', views.product_detail, name='product_detail')
]