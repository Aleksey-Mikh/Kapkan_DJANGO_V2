from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('category/<str:slug>', CategoryDetailView.as_view(), name='category'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
]
