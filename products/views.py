from django.http import HttpResponse
from django.http.response import HttpResponseRedirect



from .models import Product, Comments
from products.forms import CommentForm, ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# def index(request):
    # return HttpResponse("Hello, Welcome to the Price Comparison Tool.")



# List of products
@login_required
def products(request):
    
    context ={'products': Product.objects.all()
    }
    return render(request, "products.html", context)

# Specific product
@login_required
def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    comments = Comments.objects.filter(id=pk)

    context = {'products':products, 'comments':comments, 'pk':pk} 

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


def deletecomment(request, pk):
    
    
    
    comments = get_object_or_404(pk=pk)
    
    
    comments.delete()
    


        
    return render(request, 'deletecomment.html')

# Create your views here.
@login_required
def edit_comments(request, pk):
    
    comments = Comments.objects.get()
    
    if request.method == "GET":
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.comment = comments
            comments.save()
            
            return redirect('products')
    else:
        form = CommentForm()
    return render(request, 'edit_comments', pk)


