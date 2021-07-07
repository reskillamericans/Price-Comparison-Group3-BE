from .models import Comments
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required
def product_list(request, id):
    products = get_object_or_404(Product, id=id)
    return render(request, 'products.html', {'products': products})


@login_required
def comment_list(request, id):
    comments = get_object_or_404(Comments, id=id)
    return render(request, 'view_comment.html', {'comments': comments})


@login_required
def new_comment(request, id):
    products = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.products = products
            comment.save()
            return redirect('products', id=products.id)
    else:
        form = CommentForm()
    return render(request, 'new_comment', {'form': form})


@login_required
def edit_comment(request, id):
    products = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=products)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.products = products
            comment.save()
            return redirect('products', id=products.id)
        else:
            form = CommentForm()
        return render(request, 'edit_comment', {'form': form})


@login_required
def delete_comment(request, id):
    comment=get_object_or_404(Comments,id=id)
    comment.delete()
    form = CommentForm()
    return render(request, 'delete_comment', {'form': form})
