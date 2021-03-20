# Generated by Django 3.1.7 on 2021-03-20 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210319_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='Новый товар или нет'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_recommend',
            field=models.BooleanField(default=False, verbose_name='Рекомендую'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('available', 'есть в наличии'), ('unavailable', 'нет в наличии'), ('deliveries_are_expected', 'ожидаются поставки')], default='available', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
