from django.db import models


# Create your models here.
class SiteSliders(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان اسلایدر')
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name='آدرس اسلایدر')
    image = models.ImageField(upload_to='images/site_sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر سایت'
        verbose_name_plural = 'اسلایدر های سایت'


class SiteBanner(models.Model):
    class SiteBannerChoices(models.TextChoices):
        home_page_upside = 'home_page_up', 'صفحه اصلی_قسمت بالایی'
        home_page_downside = 'home_page_down', 'صفحه اصلی_قسمت پایینی'
        product_list = 'product_list', 'لیست محصولات'
        product_detail = 'product_detail', 'جزییات محصولات'
        blog = 'blog', 'وبلاگ'
        product_catalog = 'product_catalog', 'کاتالوگ محصولات'
        shoes = 'shoes', 'کفش ها'

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/site_banners', verbose_name='تصویر بنر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200, choices=SiteBannerChoices.choices, verbose_name='جایگاه بنر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'
