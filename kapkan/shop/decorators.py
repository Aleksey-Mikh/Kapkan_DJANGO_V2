from functools import wraps
from django.db.models import F
from django.db import transaction

from .models import Product


def counted(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        with transaction.atomic():
            path = request.path
            slug = str(path).replace('/product/', '')
            product = Product.objects.filter(slug=slug)[0]
            product.views = F('views') + 1
            product.save()
        return f(request, *args, **kwargs)
    return decorator
