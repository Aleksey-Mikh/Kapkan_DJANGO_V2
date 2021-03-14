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
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=250, verbose_name='Номер телефона')
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
    price_x_items = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество х цена', default=0)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.price_x_items = self.quantity * self.product.price
        super().save(*args, **kwargs)
        # вызов изменения общей цены
        oder_total = self.order.order_total_price.all()
        oder_total[0].save()

    def delete(self, *args, **kwargs):
        # вызов изменения общей цены
        super().delete(*args, **kwargs)
        oder_total = self.order.order_total_price.all()
        oder_total[0].save()

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'


class OrderTotalPrice(models.Model):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_total_price',)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая цена', default=0)

    def save(self, *args, **kwargs):
        order = Order.objects.get(pk=self.order_id.pk)
        self.total_price = order.get_total_cost()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Общая цена заказа'

    class Meta:
        verbose_name = 'Общая цена заказа'
