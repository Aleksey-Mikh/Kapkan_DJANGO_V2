from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
    return render(request, 'main/index.html',)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product.filter(is_published=True)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'main/category_product.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'main/product_detail.html', context)
