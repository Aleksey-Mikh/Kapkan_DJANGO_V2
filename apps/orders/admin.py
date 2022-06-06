from django.contrib import admin
from .models import Order, OrderItem, OrderTotalPrice


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fieldsets = (
        (None, {'fields': ('product', 'price', 'price_x_items', 'quantity',)}),
    )
    raw_id_fields = ['product']
    extra = 0


class OrderTotalPriceItemInline(admin.TabularInline):
    model = OrderTotalPrice
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'address', 'status',
                    'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ('status',)
    search_fields = ('last_name', 'first_name', 'id')
    inlines = [OrderItemInline, OrderTotalPriceItemInline]


admin.site.register(Order, OrderAdmin)
