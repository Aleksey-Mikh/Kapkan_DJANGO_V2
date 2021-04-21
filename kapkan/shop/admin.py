from django.contrib import admin
from .models import Product, Category, RecommendProduct, ProductGallery, ProductSale

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class RecommendProductItemInline(admin.TabularInline):
    model = RecommendProduct
    fieldsets = (
        (None, {'fields': ('recommend_product',)}),
    )
    raw_id_fields = ['recommend_product']
    extra = 0
    fk_name = "main_product"


class GalleryProductInline(admin.TabularInline):
    model = ProductGallery
    extra = 0


class SaleProductInline(admin.TabularInline):
    model = ProductSale
    extra = 0


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'get_price', 'category', 'is_published', 'views')
    search_fields = ('title', )
    list_editable = ('is_published',)
    readonly_fields = ('views', 'get_price')
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {'fields': ('category', 'title', 'slug', 'manufacturer', 'model', 'image', 'views',
                           'description', 'price', 'get_price', 'is_published', 'status')}),
        (('Ярлыки'), {
            'fields': ('is_new', 'is_hit', 'is_recommend'),
        }),
    )
    inlines = [RecommendProductItemInline, GalleryProductInline, SaleProductInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
