from django.shortcuts import render
from django.db.models import Q

from store.models import Product

def say_hello(request):
    queryset = Product.objects.order_by('title')

    return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
