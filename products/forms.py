from django import forms
from .models import Comments
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'price','image', 'description')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = Comments
        fields = ['content', 'product']

    def __str__(self):
        return f"{self} by {self.content}"
