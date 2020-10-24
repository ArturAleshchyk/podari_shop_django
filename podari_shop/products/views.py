from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from products.models import Product, Category


def index(req):
    categories = Category.objects.all()
    products = Product.objects.all()
    last_products = Product.objects.order_by('pk').reverse()[:8]

    return render(req, 'products/index.html', {
        'categories': categories,
        'products': products,
        'title': 'Главная страница',
        'last_products': last_products
    })


def get_category(req, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.all()

    return render(req, 'products/category.html', {
        'categories': categories,
        'category': category,
        'products': products
    })
