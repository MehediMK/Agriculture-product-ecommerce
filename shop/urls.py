from django.urls import path
from .views import (index, reply, shop, product_detail, user_product, add_product, edit_product, delete_product,
                    add_cart, cartlist, cart_item_pop, checkout)

# for sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
# model import
from shop.models import Product

info_dict = {
    'queryset': Product.objects.all(),
}

urlpatterns = [
    path('', index, name='index'),
    path('reply/', reply, name='reply'),
    path('products-list/', shop, name='shop'),
    path('add-cart/', add_cart, name='add_cart'),
    path('products-cart/', cartlist, name='cartlist'),
    path('products-checkout/', checkout, name='checkout'),
    path('user-product/', user_product, name='user_product'),
    path('add-product/', add_product, name='add_product'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path('cart-remove/<int:id>/', cart_item_pop, name='cart_item_pop'),
    path('product-detail/<int:id>/', product_detail, name='product_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': {'products': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]
