# Generated by Django 5.0.1 on 2024-01-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_articlegallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlegallery',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='articlegallery',
            name='image_3',
        ),
        migrations.AlterField(
            model_name='articlegallery',
            name='image',
            field=models.ImageField(upload_to='images/articles/article_gallery', verbose_name='تصویر مقاله'),
        ),
    ]
