# Generated by Django 3.1.7 on 2021-04-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopvideo',
            name='templates_video_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на видео'),
        ),
    ]
