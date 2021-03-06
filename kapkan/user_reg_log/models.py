from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)