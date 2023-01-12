from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_pagination(products, context: dict, number_page: int, number_items_view: int):
    """ 
    get number_page 
    display number_items_view
    """
    products_paginator = Paginator(products, number_items_view)
    try:
        products = products_paginator.page(number_page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)
    context.update({'products': products})
    return context
