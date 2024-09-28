from django.db import models
from django.forms import ModelForm
from django.utils.text import slugify
from account_module.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True, unique=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    short_description = models.TextField(verbose_name='توضیحات کوتاه محصول')
    description = models.TextField(verbose_name='توضیحات اصلی')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده', editable=False)
    category = models.ManyToManyField('ProductCategory', related_name='product_categories',
                                      verbose_name='دسته بندی های محصول')
    brand = models.ForeignKey('ProductBrand', on_delete=models.CASCADE, verbose_name='برند محصول')
    favorite = models.ManyToManyField(User, related_name='product_favorites', verbose_name='علاقه مندی ها', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} / {self.price}'

    def parents(self):
        return ",".join([str(p) for p in self.category.all()])

    def __unicode__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='دسته بندی والد', null=True,
                               blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    image = models.ImageField(upload_to='images/product_categories', verbose_name='تصویر دسته بندی')
    image_two = models.ImageField(upload_to='images/product_categories', verbose_name='تصویر دوم دسته بندی')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, db_index=True, verbose_name='حذف شده / نشده')
    gender = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='برای کدام جنسیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام برند')
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='فعال / غیر فعال')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='برای کدام محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر محصول')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'گالری تصویر'
        verbose_name_plural = 'گالری تصاویر'


class Person(models.Model):
    gender = models.CharField(max_length=50, verbose_name='جنسیت')
    image = models.ImageField(upload_to='images/women_catalog', verbose_name='تصویر شخص')
    url_title = models.CharField(max_length=50, verbose_name='عنوان در url')

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = 'جنسیت '
        verbose_name_plural = 'جنسیت ها'


class Shoes(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True, unique=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/shoes', verbose_name='تصویر محصول')
    price = models.CharField(max_length=100, verbose_name='قیمت')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    short_description = models.TextField(verbose_name='توضیحات کوتاه محصول')
    description = models.TextField(verbose_name='توضیحات اصلی')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده', editable=False)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند')
    category = models.ForeignKey('ShoesCategory', on_delete=models.CASCADE, verbose_name='برای دسته بندی')
    favorite = models.ManyToManyField(User, related_name='shoes_favorites', verbose_name='علاقه مندی ها', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} / {self.price}'

    class Meta:
        verbose_name = 'کفش'
        verbose_name_plural = 'کفش ها'


class ShoesCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    image = models.ImageField(upload_to='images/shoes_categories', verbose_name='تصویر دسته بندی')
    image_two = models.ImageField(upload_to='images/shoes_categories', verbose_name='تصویر دوم دسته بندی')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, db_index=True, verbose_name='حذف شده / نشده')
    gender = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='جنسیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی کفش'
        verbose_name_plural = 'دسته بندی های کفش'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='پوشاک')
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کفش')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    parent = models.ForeignKey('ProductComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')
    text = models.TextField(verbose_name='متن')

    def __str__(self):
        if self.product:
            return str(self.product.title)
        else:
            return str(self.shoes.title)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    ip = models.CharField(max_length=30, verbose_name='آی پی')

    def __str__(self):
        return f'{self.user} / {self.ip}'

    class Meta:
        verbose_name = 'بازید محصول'
        verbose_name_plural = 'بازیدهای محصول'
