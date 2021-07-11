from .models import Product, Comments
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'description', 'miscellaneous')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('product', 'comment', 'user')

