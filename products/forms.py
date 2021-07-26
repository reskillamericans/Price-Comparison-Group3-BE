
  
from django import forms
from .models import Comments
from .models import Product


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
        fields = ['content']


class AddProductForm(forms.Form):
    """
    Adds products. Used with add product view and template
    """
    amazon_asin = forms.CharField(max_length=12)
    ebay_url = forms.CharField(max_length=200)

