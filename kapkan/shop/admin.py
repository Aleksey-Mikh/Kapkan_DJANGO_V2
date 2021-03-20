from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'is_published',)
    search_fields = ('title', )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {'fields': ('category', 'title', 'slug', 'image', 'description', 'price', 'is_published', 'status')}),
        (('Ярлыки'), {
            'fields': ('is_new', 'is_recommend',),
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)