from django.db import models
from shop.models import Product


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
    )

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата измения')
    status = models.CharField(
        max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW
    )
    comment_for_order = models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Заказ')
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.PROTECT,
        verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая цена', default=0)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ord = self.order.pk
        order = Order.objects.get(pk=ord)
        order_item_base = order.items.last()
        print(order_item_base.total_price)
        if order_item_base.total_price == 0:
            print('/////////////////////////////')
            print(self.price, self.product.price, self.order.pk)
            self.price = self.product.price
            print(order_item_base.total_price)
            print('/////////////////////////////')
            super().save(*args, **kwargs)
