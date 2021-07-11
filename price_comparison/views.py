from django.http import HttpResponse
from .models import Product, Comments
from .forms import CommentForm
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView


# Create your views here.
def product_detail(request, slug):
    template_name = 'new.comment.html'
    product = get_object_or_404(Product, slug=slug)
    comments = product.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})