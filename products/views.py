from django.shortcuts import render
from .models import Product
import datetime

def product_detail(request):
    return render(request, 'product-detail.html')

def products(request):
    products = Product.objects.all().order_by('order_id')
    new_products = products.filter(created_date__month=datetime.datetime.now().month, created_date__year=datetime.datetime.now().year )
    popular_products = products.filter(is_popular=True)
    context = {
       'products' : products,
       'new_products' : new_products,
       'popular_products' : popular_products
    }
    
    return render(request, 'products.html', context)

