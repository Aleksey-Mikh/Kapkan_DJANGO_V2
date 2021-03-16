from django.db import models
from django.urls import reverse


class Product(models.Model):

    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, related_name='product')
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos/%Y/%m', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category']


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
