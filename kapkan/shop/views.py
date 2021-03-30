from datetime import datetime, timezone

from django.core.paginator import Paginator
from django.db.models import Count, F, Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category
from cart.forms import CartAddProductForm
from .forms import ProductFilterForm


# Время (в часах) сколько товар будет стоять с ярлыком NEW
TIME_IS_NEW = 20


def filter_product(request, products, **kwargs):
    if request.method == 'GET':
        form = ProductFilterForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['min_price']:
                products = products.filter(price__gte=form.cleaned_data['min_price'])
            if form.cleaned_data['max_price']:
                products = products.filter(price__lte=form.cleaned_data['max_price'])
            if form.cleaned_data['is_new']:
                products = products.filter(is_new=form.cleaned_data['is_new'])
            if form.cleaned_data['is_hit']:
                products = products.filter(is_hit=form.cleaned_data['is_hit'])
            if form.cleaned_data['is_recommend']:
                products = products.filter(is_recommend=form.cleaned_data['is_recommend'])
    else:
        form = ProductFilterForm()
    context = {
        'products': products,
        'form': form,
    }
    return context


class IndexView(ListView):

    model = Category
    template_name = 'shop/index.html'
    context_object_name = 'categori'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_recommend=True)
        context['title'] = 'Главная'
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

    def get_queryset(self):
        return super(IndexView, self).get_queryset().annotate(cnt=Count(
            'product', filter=F('product__is_published'))).filter(cnt__gt=0).order_by('name')


class CategoryDetailView(ListView):

    model = Product
    template_name = 'shop/category_product.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(Q(is_new=True) & Q(category=category))
        if products:
            time_now = datetime.now(timezone.utc)
            for product in products:
                time_then = product.created
                time_delta = time_now - time_then
                if (time_delta.total_seconds() // 3600) > TIME_IS_NEW:
                    product.is_new = False
                    product.save()
        return category.product.filter(is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cart_product_form'] = cart_product_form
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = category.product.filter(is_published=True).select_related('category')
        context_2 = filter_product(self.request, products)
        context.update(context_2)
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
    paginate_by = 12

    def get_queryset(self):
        products = Product.objects.filter(Q(is_new=True) & Q(title__icontains=self.request.GET.get('s')))
        if products:
            time_now = datetime.now(timezone.utc)
            for product in products:
                time_then = product.created
                time_delta = time_now - time_then
                if (time_delta.total_seconds() // 3600) > TIME_IS_NEW:
                    product.is_new = False
                    product.save()
        return Product.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['search'] = self.request.GET.get('s')
        return context


