# Generated by Django 3.1.7 on 2021-04-22 12:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('image', models.ImageField(upload_to='photos/%Y/%m', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('manufacturer', models.CharField(blank=True, max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(blank=True, max_length=255, verbose_name='Модель')),
                ('image', models.ImageField(upload_to='photos/%Y/%m', verbose_name='Основное изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('status', models.CharField(choices=[('available', 'есть в наличии'), ('unavailable', 'нет в наличии'), ('deliveries_are_expected', 'ожидаются поставки')], default='available', max_length=100, verbose_name='Статус заказа')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_new', models.BooleanField(default=True, verbose_name='NEW')),
                ('is_hit', models.BooleanField(default=False, verbose_name='ХИТ')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='Рекомендованно')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ShopVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=255, verbose_name='Название видео')),
                ('video_link', models.CharField(max_length=255, verbose_name='Ссылка на видео')),
                ('video_description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='RecommendProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='shop.product', verbose_name='Основной товар')),
                ('recommend_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommend_product', to='shop.product', verbose_name='Рекомендованный товар')),
            ],
            options={
                'verbose_name': 'Рекомендованный товар',
                'verbose_name_plural': 'Рекомендованные товары',
            },
        ),
        migrations.CreateModel(
            name='ProductSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка, %')),
                ('product_with_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_with_sale', to='shop.product')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_gallery', models.ImageField(upload_to='photos/%Y/%m', verbose_name='Дополнительные изображения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Дополнительное изображение',
                'verbose_name_plural': 'Дополнительные изображения',
            },
        ),
    ]
