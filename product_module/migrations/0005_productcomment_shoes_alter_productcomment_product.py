# Generated by Django 5.0.1 on 2024-01-23 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='shoes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.shoes', verbose_name='کفش'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='پوشاک'),
        ),
    ]
