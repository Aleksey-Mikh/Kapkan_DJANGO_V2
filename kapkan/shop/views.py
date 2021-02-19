from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm



def index(request):
    return render(request, 'shop/index.html',)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product.filter(is_published=True)
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'category': category,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/category_product.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product_detail.html', context)
