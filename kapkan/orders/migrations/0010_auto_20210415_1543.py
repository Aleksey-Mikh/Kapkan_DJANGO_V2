# Generated by Django 3.1.7 on 2021-04-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Скидка'),
        ),
    ]
