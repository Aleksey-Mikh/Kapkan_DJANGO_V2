from django.urls import path
from .views import IndexView, CategoryDetailView, ProductDetailView, empty_cart, SearchView, about_us


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('category/<str:slug>', CategoryDetailView.as_view(), name='category'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('empty_cart/', empty_cart, name='empty_cart'),
    path('about_us/', about_us, name='about_us'),
    path('search/', SearchView.as_view(), name='search'),
]
