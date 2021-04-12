import decimal

from django.db import models
from django.urls import reverse


class ProductSale(models.Model):
    product_with_sale = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_with_sale')
    sale = models.IntegerField(verbose_name='Скидка, %')

    def __str__(self):
        return f'Скидка {self.sale} %'

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Product(models.Model):

    STATUS_AVAILABLE = 'available'
    STATUS_UNAVAILABLE = 'unavailable'
    STATUS_DELIVERIES = 'deliveries_are_expected'

    STATUS_CHOICES = (
        (STATUS_AVAILABLE, 'есть в наличии'),
        (STATUS_UNAVAILABLE, 'нет в наличии'),
        (STATUS_DELIVERIES, 'ожидаются поставки'),
    )

    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, related_name='product')
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    manufacturer = models.CharField(max_length=255, verbose_name="Производитель", blank=True)
    model = models.CharField(max_length=255, verbose_name="Модель", blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m', verbose_name='Основное изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    status = models.CharField(
        max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_AVAILABLE
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_new = models.BooleanField(default=True, verbose_name='NEW')
    is_hit = models.BooleanField(default=False, verbose_name='ХИТ')
    is_recommend = models.BooleanField(default=False, verbose_name='Рекомендованно')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_price(self):
        sale = self.product_with_sale.first()
        if sale:
            price = self.price - self.price * decimal.Decimal((sale.sale / 100))
            return round(price, 2)
        return self.price

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class ProductGallery(models.Model):
    image_gallery = models.ImageField(upload_to='photos/%Y/%m', verbose_name='Дополнительные изображения')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return 'Дополнительные изображения'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


class RecommendProduct(models.Model):

    main_product = models.ForeignKey(
        Product,
        related_name='main_product',
        on_delete=models.CASCADE,
        verbose_name='Основной товар')
    recommend_product = models.ForeignKey(
        Product,
        related_name='recommend_product',
        on_delete=models.CASCADE,
        verbose_name='Рекомендованный товар')

    def __str__(self):
        return 'Рекомендованный товар'

    class Meta:
        verbose_name = 'Рекомендованный товар'
        verbose_name_plural = 'Рекомендованные товары'


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    image = models.ImageField(upload_to='photos/%Y/%m', verbose_name='Изображение')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

