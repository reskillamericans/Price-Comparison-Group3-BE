from django.urls import path
from . import views
# Paths

urlpatterns = [
    path('', views.main, name = 'main'),
    path('', views.index, name ='index')
]
