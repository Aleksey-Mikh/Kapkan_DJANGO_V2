from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category
from cart.forms import CartAddProductForm


class IndexView(ListView):

    model = Category
    template_name = 'shop/index.html'
    context_object_name = 'categori'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        return super(IndexView, self).get_queryset().order_by('name')


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


def empty_cart(request):
    return render(request, 'shop/empty_cart.html')


class SearchView(ListView):
    template_name = 'shop/search.html'
    context_object_name = 'products'
    #paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['search'] = self.request.GET.get('s')
        return context
