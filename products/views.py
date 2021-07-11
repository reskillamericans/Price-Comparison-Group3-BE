from django.db.models.query import QuerySet
from django.http import request
from .models import Comments
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView




# List of Products

def base(request):
        welcome = print("rendering index for main website")
        return render(request, 'base.html', welcome)

def products(request):
    querySet = Product.objects.get_queryset()
    
    context = {'product_list':querySet}
        
    
    return render(request, "products/products.html", context)

# View Single Product

def retrieveproduct(request, pk):

    context = {}
    context['data'] = Product.objects.get(id=pk)
    
    
    
    return render(request, "retrieveproduct.html", context)
    
def viewcomments(request, Comments):
    
    context = {}
    form = CommentForm(request.GET or None)

    context['morecomments'] = Comments.objects.get(id=products)

    return render(request, "viewcomments.html", context)

def addcomments(request):
    context = {}
    CommentForm(request.POST or None)
    context['entry'] =Comments.objects.filter()
    
    
    return render(request, "addcomments.html", context)



def edit_comment(request):
    edit_comment =Comments.objects.get()
    return render(request, "edit_comment.html")

def delete_comment(request, self):
    delete_comment =Comments.objects.get(self)

    return render(request, "delete_comment.html",{'delete_comment':delete_comment} )



