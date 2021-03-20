from django.db import models
from django.urls import reverse


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
    image = models.ImageField(upload_to='photos/%Y/%m', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    status = models.CharField(
        max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_AVAILABLE
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_new = models.BooleanField(default=True, verbose_name='Новый товар или нет')
    is_recommend = models.BooleanField(default=False, verbose_name='Рекомендую')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


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
