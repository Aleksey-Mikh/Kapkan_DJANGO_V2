# Generated by Django 3.1.7 on 2021-03-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price_x_items',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]