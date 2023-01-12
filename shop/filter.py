from .models import (Product)

def product_search(category=None, search=None, session_sortby=None, min_price=None, max_price=None):
    products = []
    if category:
        if session_sortby == 'desc':
            products = Product.objects.filter(product_category__id = category).order_by('-create_date')
        elif session_sortby == 'htol':
            products = Product.objects.filter(product_category__id = category).order_by('-product_price')
        elif session_sortby == 'ltoh':
            products = Product.objects.filter(product_category__id = category).order_by('product_price')
        else:
            products = Product.objects.filter(product_category__id = category).order_by('create_date')

    elif min_price and max_price:
        if session_sortby == 'desc':
            products = Product.objects.filter(product_price__gte = min_price , product_price__lte = max_price).order_by('-create_date')
        elif session_sortby == 'htol':
            products = Product.objects.filter(product_price__gte = min_price , product_price__lte = max_price).order_by('-product_price')
        elif session_sortby == 'ltoh':
            products = Product.objects.filter(product_price__gte = min_price , product_price__lte = max_price).order_by('product_price')
        else:
            products = Product.objects.filter(product_price__gte = min_price , product_price__lte = max_price).order_by('create_date')

    elif search:
        if session_sortby == 'desc':
            products = Product.objects.filter(product_title__icontains = search).order_by('-create_date')
        elif session_sortby == 'htol':
            products = Product.objects.filter(product_title__icontains = search).order_by('-product_price')
        elif session_sortby == 'ltoh':
            products = Product.objects.filter(product_title__icontains = search).order_by('product_price')
        else:
            products = Product.objects.filter(product_title__icontains = search).order_by('create_date')
    else:
        if session_sortby == 'desc':
            products = Product.objects.all().order_by('-create_date')
        elif session_sortby == 'htol':
            products = Product.objects.all().order_by('-product_price')
        elif session_sortby == 'ltoh':
            products = Product.objects.all().order_by('product_price')
        else:
            products = Product.objects.all().order_by('create_date')

    return products