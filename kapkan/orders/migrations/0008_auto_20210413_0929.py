# Generated by Django 3.1.7 on 2021-04-13 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210314_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordertotalprice',
            options={'verbose_name': 'Общая цена заказа', 'verbose_name_plural': 'Общая цена заказа'},
        ),
    ]
