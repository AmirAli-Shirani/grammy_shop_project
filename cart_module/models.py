from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='نهایی شده / نشده')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ نهایی شده')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید کاربران'
        verbose_name_plural = 'لیست سبد های خرید کاربران'


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.cart)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبد های خرید'
