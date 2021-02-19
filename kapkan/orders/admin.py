from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'address', 'city', 'status',
                    'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ('status',)
    search_fields = ('last_name', 'first_name')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
