# Generated by Django 5.0.1 on 2024-01-21 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0003_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/articles/article_gallery', verbose_name='تصویر اول مقاله')),
                ('image_2', models.ImageField(upload_to='images/articles/article_gallery', verbose_name='تصویر دوم مقاله')),
                ('image_3', models.ImageField(upload_to='images/articles/article_gallery', verbose_name='تصویر سوم مقاله')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.article', verbose_name='برای کدام مقاله')),
            ],
            options={
                'verbose_name': 'تصویر مقاله',
                'verbose_name_plural': 'تصاویر مقاله',
            },
        ),
    ]
