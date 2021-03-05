# Generated by Django 3.1.7 on 2021-03-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=250, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
