from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product, Category


def index(req):
    categories = Category.objects.all()
    products = Product.objects.all()
    last_products = Product.objects.order_by('pk').reverse()[:8]

    return render(req, 'products/index.html', {
        'categories': categories,
        'products': products,
        'title': 'Главная',
        'last_products': last_products
    })
