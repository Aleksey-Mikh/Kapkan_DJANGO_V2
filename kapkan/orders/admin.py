from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # n = model.objects.filter(pk=1)
    # for n in n:
    #     print(n.order)
    raw_id_fields = ['product']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'address', 'status',
                    'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ('status',)
    search_fields = ('last_name', 'first_name')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
