from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان تماس با ما')
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    numbers = models.CharField(max_length=50, verbose_name='شماره همراه')
    message = models.TextField(verbose_name='متن پیام تماس با ما')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')
    create_day = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
