from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from orders.models import Order


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    orders = models.ManyToManyField(Order, verbose_name='Заказы покупателя')

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)