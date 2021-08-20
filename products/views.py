import json
import environ

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic

from test_files import ebay_products, amazon_products
from .forms import AddProductForm, CommentForm
from .models import Product, LikeButton, Comment

# Debug product fetching
env = environ.Env()
environ.Env.read_env()

# Debug product fetching
debug_gp = env.bool('DEBUG_GP')
amazon_responses = amazon_products.amazon_responses
ebay_responses = ebay_products.ebay_responses


class LandingPage(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('product_name')[:10]


@login_required
def product_list(request, id):
    products = get_object_or_404(Product, id=id)
    return render(request, 'products.html', {'products': products})


# Show list of products
class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('product_name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # For displaying rows
        products = self.object_list
        count = products.count()
        iterations = int(count / 5)
        if count % 5 > 0:
            iterations += 1
        slices = []
        for i in range(iterations):
            slices.append(f"{i * 5}:{5 * (i + 1)}")
        context['slices'] = slices
        return context


# Show product details
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['likes'] = LikeButton.objects.filter(product_id=pk).first()
        user = self.request.user
        if user.is_authenticated:
            context['user_like'] = LikeButton.objects.filter(user=self.request.user, product_id=pk)
        else:
            context['user_like'] = False

        # Split features into list of lines
        product = self.object
        features = product.description.splitlines()
        context['list_lines'] = features

        return context


# Show product modal
class ProductModalView(generic.DetailView):
    model = Product
    template_name = 'products/Modal.html'

    def get_context_data(self, **kwargs):
        context = super(ProductModalView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['likes'] = LikeButton.objects.filter(product_id=pk).first()
        context['comment_list'] = Comment.objects.filter(product=pk)
        user = self.request.user
        if user.is_authenticated:
            context['user_like'] = LikeButton.objects.filter(user=self.request.user, product_id=pk)
        else:
            context['user_like'] = False

        context['comment_list'] = Comment.objects.filter(product_id=pk)
        return context


# Like button
def like_button(request):
    if request.method == "POST":
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            likes_id = request.POST.get("likes_id", None)
            like_object = get_object_or_404(LikeButton, pk=likes_id)

            # Check if user already liked product
            if like_object.user.filter(id=request.user.id):
                # Remove user like from product
                like_object.user.remove(request.user)
                liked = False
            else:
                # Add user like to product
                like_object.user.add(request.user)
                liked = True

            # Create new context to feed back to AJAX call
            context = {"likes_count": like_object.total_likes,
                       "user_like"  : liked,
                       "likes_id"   : likes_id
                       }
            return HttpResponse(json.dumps(context), content_type='application/json')


def add_product_view(request):
    # Check if request was POST
    if request.method == 'POST':
        # Get amazon_asin & ebay_url
        amazon_asin = request.POST.get('amazon_asin')
        ebay_url = request.POST.get('ebay_url')

        # Get respective data
        amazon_product = get_amazon_product(amazon_asin)
        ebay_product = get_ebay_product(ebay_url)

        # Get or create product
        product, created = get_create_product(amazon_product, ebay_product)

        if product:
            if not created:
                messages.success(request, f"\"{product.product_name}\" has been updated")
            else:
                messages.success(request, f"\"{product.product_name}\" has been created")
        else:
            messages.error(request, f"Error: {created}")

    # Render page with any bound data and error messages
    context = {'form': AddProductForm(), 'product_list': Product.objects.order_by('id')}
    return render(request, 'products/add_product.html', context)


def delete_product(request, product_id):
    # Retrieve product
    product = get_object_or_404(Product, pk=product_id)
    product_name = product.product_name
    # Delete product
    product.delete()
    messages.success(request, f"\"{product_name}\" has been deleted")
    return redirect('products:add_product')


# Get amazon product from asin
def get_amazon_product(amazon_asin):
    url = env('AMAZON_URL')
    querystring = {"country": "US", "asin": amazon_asin}
    headers = {'x-rapidapi-key' : env('AMAZON_KEY'),
               'x-rapidapi-host': env('AMAZON_HOST')}

    if debug_gp:
        response = amazon_responses[int(amazon_asin)]
    else:
        response = requests.request("GET", url, headers=headers, params=querystring).json()

    amazon_context = {
        'asin'       : response['asin'],
        'price'      : response['prices']['current_price'],
        'description': response['description'],
        'features'   : response['features'],
        'image_urls' : response['images'],
        'url'        : response['full_link']
        }
    while None in amazon_context['features']:
        amazon_context['features'].remove(None)
    return amazon_context


# Get ebay product from url
def get_ebay_product(ebay_url):
    url = env('EBAY_URL')
    querystring = {"URL": ebay_url}
    headers = {'x-rapidapi-key' : env('EBAY_KEY'),
               'x-rapidapi-host': env('EBAY_HOST')}

    if debug_gp:
        response = ebay_responses[int(ebay_url)]
    else:
        response = requests.request("GET", url, headers=headers, params=querystring).json()

    ebay_context = {
        'name'      : response['title'],
        'price'     : response['prices']['current_price'],
        'url'       : response['full_link'],
        'image_urls': response['images'],
        'category'  : response['category'],
        }
    return ebay_context


# Get or crete product
def get_create_product(amazon_product, ebay_product):
    # Try to find a valid image url
    image_url = staticfiles_storage.url("/images/product_images/image_not_found.png")
    for image in amazon_product['image_urls'] + ebay_product['image_urls']:
        if image:
            image_url = image
            break

    # Create a product
    try:
        product, created = Product.objects.update_or_create(
                amazon_asin=amazon_product['asin'],
                defaults={'product_name': ebay_product['name'],
                          'description' : amazon_product['description'],
                          'amazon_price': amazon_product['price'],
                          'ebay_price'  : ebay_product['price'],
                          'amazon_url'  : amazon_product['url'],
                          'ebay_url'    : ebay_product['url'],
                          'category'    : ebay_product['category'],
                          'features'    : amazon_product['features'],
                          'image'       : image_url,
                          }
                )

        # Save product (to generate product pk)
        product.save()

        # Return product, created
        return product, created
    except ValidationError as e:
        return False, e
    except LookupError as e:
        return False, e


# Add comment to product
@login_required(login_url="signup")
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content')
        comment = Comment(user=user, content=content, product=product, approved=True)
        comment.save()
        messages.success(request, 'Comment successfully added.')
    return redirect('products:product_modal', pk=product.pk)


# Delete comment
@login_required(login_url="signup")
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    product = get_object_or_404(Product, pk=comment.product.pk)
    comment.delete()
    messages.success(request, 'Comment successfully deleted.')
    return redirect('products:product_modal', pk=product.pk)


# Edit Comment
@login_required(login_url="signup")
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = CommentForm(instance=comment)

    if request.method == 'POST' and 'Update' in request.POST:
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated = True
            comment.last_update = timezone.now()
            comment.save()
            messages.success(request, 'Comment was successfully edited.')
            return redirect('products:product_modal', pk=comment.product.pk)
    elif request.method == 'POST' and 'Cancel' in request.POST:
        return redirect('products:product_modal', pk=comment.product.pk)

    context = {'form': form, 'comment': comment}
    return render(request, 'edit_comment.html', context)


# Show product comments
class ProductComments(generic.DetailView):
    model = Product
    template_name = 'comment_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductComments, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['form'] = CommentForm
        context['comment_list'] = Comment.objects.filter(product_id=pk)
        return context
