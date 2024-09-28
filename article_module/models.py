from django.db import models
from django.utils.text import slugify

from account_module.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    slug = models.SlugField(max_length=300, allow_unicode=True, null=False, verbose_name='عنوان در url')
    short_description = models.TextField(verbose_name='توضیحات نقل قول')
    blockquote = models.TextField(verbose_name='نقل قول')
    paragraph = models.TextField(verbose_name='سطر های مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='برای کدام مقاله')
    image = models.ImageField(upload_to='images/articles/article_gallery', verbose_name='تصویر مقاله')

    def __str__(self):
        return str(self.article.title)

    class Meta:
        verbose_name = 'تصویر مقاله'
        verbose_name_plural = 'تصاویر مقاله'


class ArticleHeading(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    slug = models.SlugField(max_length=300, allow_unicode=True, null=False, verbose_name='عنوان در url')
    blockquote = models.TextField(verbose_name='نقل قول')
    short_description = models.TextField(verbose_name='توضیحات نقل قول')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'مقاله بالایی'
        verbose_name_plural = 'مقالات بالایی'
