from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection'] #we can use the below function to do the same thing

    # def collection_title(self, product):
    #     return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    ordering = ['placed_at']
    list_per_page = 10
    list_select_related = ['customer']

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        '''returning an html content eg: link, imported at the top'''
        return format_html('<a href="https://google.com">{}</a>', collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

# Register your models here.
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)