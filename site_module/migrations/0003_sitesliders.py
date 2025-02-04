# Generated by Django 5.0.1 on 2024-01-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_sitebanner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان اسلایدر')),
                ('sub_title', models.CharField(max_length=200, verbose_name='عنوان کوچک اسلایدر')),
                ('image', models.ImageField(upload_to='images/site_sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'اسلایدر سایت',
                'verbose_name_plural': 'اسلایدر های سایت',
            },
        ),
    ]
