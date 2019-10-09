# Generated by Django 2.2.5 on 2019-09-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190908_2250'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='item',
            name='news_item_created_f2b812_idx',
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['points', 'created_at'], name='news_item_points_d03885_idx'),
        ),
    ]
