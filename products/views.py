from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


# list view
def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "products.html", context)

def product_detail(request, pk):

    context ={}

    context["data"] = Product.objects.get(pk=pk)

    return render(request, "product_detail.html", context)










