from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'product_price', 'discount_price', 'product_category',
                  'product_image', 'product_description', 'quantity', 'unit', 'post_type')
