# Generated by Django 3.1.7 on 2021-05-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210428_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopAdminConst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIME_IS_NEW', models.CharField(max_length=255, verbose_name='Время (в часах) которое товар находится в статусе NEW')),
                ('EMAIL_ADMIN_CONFED', models.CharField(max_length=255, verbose_name='E-MAIL на который будут приходить оповещения о заказах')),
                ('EMAIL_ADMIN_PASSWORD_CONFED', models.CharField(max_length=255, verbose_name='Пароль от E-MAIL')),
            ],
            options={
                'verbose_name': 'Администрация констат сайта',
                'verbose_name_plural': 'Администрация констат сайта',
            },
        ),
    ]
