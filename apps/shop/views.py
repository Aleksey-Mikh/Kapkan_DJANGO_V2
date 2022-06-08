from datetime import datetime, timezone

from django.db.models import Count, F, Q
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Product, Category, RecommendProduct, ShopVideo
from cart.forms import CartAddProductForm
from .forms import ProductFilterForm
from .decorators import counted


# The time while the product is in the "New" status
# TIME_IS_NEW = ShopAdminConst.objects.first().TIME_IS_NEW


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
        context['products'] = Product.objects.prefetch_related('product_with_sale').filter(is_recommend=True)
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
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(Q(is_new=True) & Q(category=self.category)).select_related('category')
        if products:
            time_now = datetime.now(timezone.utc)
            for product in products:
                time_then = product.created
                time_delta = time_now - time_then
                if (time_delta.total_seconds() // 3600) > 0:
                    product.is_new = False
                    product.save()
        return self.category.product.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['title'] = self.category
        context['cart_product_form'] = cart_product_form
        products = self.category.product.filter(is_published=True)
        context_2 = filter_product(self.request, products)
        context.update(context_2)
        return context


@method_decorator(counted, name='dispatch')
class ProductDetailView(DetailView):

    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        product = Product.objects.get(slug=self.kwargs['slug'])
        context['title'] = product
        context['cart_product_form'] = cart_product_form
        print(product)
        product_sale = product.product_with_sale.first()
        if product_sale:
            context['product_sale'] = product_sale.sale
        product_images = product.images.all()
        if product_images:
            context['product_images'] = product_images
        recommend_products = RecommendProduct.objects.select_related(
            "recommend_product").filter(main_product=product)
        if recommend_products:
            context['recommend_products'] = recommend_products

        empty_last_product = list()
        last_products = self.request.session.get('last_products', empty_last_product)
        if product.pk not in last_products:
            last_products.insert(0, product.pk)
        if len(last_products) >= 5:
            last_products = last_products[:5]
        self.request.session['last_products'] = last_products
        if last_products:
            last_products_in_temple = []
            for last in last_products:
                last_products_in_temple.append(Product.objects.prefetch_related().filter(id=last))
            context['last_products_in_temple'] = last_products_in_temple
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
                if (time_delta.total_seconds() // 3600) > 0:
                    product.is_new = False
                    product.save()
        return Product.objects.prefetch_related('product_with_sale').filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['search'] = self.request.GET.get('s')
        return context


def about_us(request):
    return render(request, 'shop/about_us.html')


def contacts(request):
    return render(request, 'shop/contacts.html')


def video(request):
    title = 'Видео'
    video_for_template = ShopVideo.objects.all()
    context = {
        'video_for_template': video_for_template,
        'title': title,
    }
    return render(request, 'shop/video.html', context)
