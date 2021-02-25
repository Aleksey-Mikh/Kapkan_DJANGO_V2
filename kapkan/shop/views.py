from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category
from cart.forms import CartAddProductForm


class IndexView(ListView):

    # потом добавить на главный экран вывод категорий в 'картах', а не статичные заглушки
    model = Category
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class CategoryDetailView(ListView):

    model = Product
    template_name = 'shop/category_product.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.product.filter(is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cart_product_form'] = cart_product_form
        return context


class ProductDetailView(DetailView):

    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['title'] = Product.objects.get(slug=self.kwargs['slug'])
        context['cart_product_form'] = cart_product_form
        return context
