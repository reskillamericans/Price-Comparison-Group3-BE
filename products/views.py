
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Comments
from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required




# List of products

def products(request):
    
    context ={'products': Product.objects.all()[:10]
    }
    
    return render(request, "products.html", context)

# Specific product detail

def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    
    context = {'products':products,'pk':pk} 

    return render(request, "product_detail.html", context)

# Add comment to product
@login_required
def add_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
       
        user=request.user
        content=request.POST.get('comment_body')
        comments=Comments(user=user, content=content, product=product)
        comments.save()
        
        return redirect('product_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'pk':pk})

# Delete comment
@login_required
def deletecomment(request, id, pk):
    context={}
    comments = get_object_or_404(Comments, id=id)
    product = get_object_or_404(Product, pk=pk)
    request.user=comments.user
    if request.method =="POST":
        comments.delete()
        return HttpResponseRedirect(reverse('product_detail', kwargs={"pk": product.pk}))
    else:
        return render(request, "deletecomment.html", context)


# Edit Comment
@login_required
def edit_comments(request, id, pk):
    
    product = get_object_or_404(Product, pk=pk)
    comments = Comments.objects.get(id=id)
    if request.method == 'POST':
        request.user=comments.user
        form = CommentForm(request.POST, instance=comments)
        
        form.save()
            
        return HttpResponseRedirect(reverse('product_detail', kwargs={"pk": product.pk}))
    else:
        form=CommentForm(instance=comments)
    return render(request, 'edit_comments.html', {'form':form, 'comments':comments, 'pk':pk})


