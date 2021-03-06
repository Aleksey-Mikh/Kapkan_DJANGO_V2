# Generated by Django 3.1.7 on 2021-04-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shopvideo_templates_video_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopvideo',
            old_name='video_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='shopvideo',
            old_name='video_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='shopvideo',
            old_name='video_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='shopvideo',
            name='templates_video_link',
        ),
        migrations.AddField(
            model_name='shopvideo',
            name='templates_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на видео для шаблона'),
        ),
    ]
