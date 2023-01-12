from django.contrib import admin
from .models import (Product, Category, Carousel, OrderPlace, BeatItem)


admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(BeatItem)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'product_title', 'product_category',
                    'product_price', 'discount_price', 'create_date']
    search_fields = ('user__username', 'product_title',
                     'product_category__category_name', 'create_date')
    list_editable = ['product_price', 'discount_price']
    list_display_links = ['pk', 'user']


@admin.register(OrderPlace)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'product', 'quantity', 'email',
                    'mobile', 'address', 'total_price', 'status', 'TrxID']
    search_fields = ('product', 'user', 'email', 'mobile', 'TrxID', 'city')
    list_editable = ['status']
    list_display_links = ['user', 'product']
