from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product, Category


def index(req):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(req, 'products/index.html', {
        'categories': categories,
        'products': products,
        'title': 'Главная'
    })
