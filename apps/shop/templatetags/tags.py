from django import template
from django.db.models import Count, F

from apps.shop.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.annotate(
        cnt=Count('product', filter=F('product__is_published'))).filter(cnt__gt=0).order_by('name')
