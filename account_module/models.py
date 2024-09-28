from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/user_avatars', verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=200, verbose_name='کد فعالسازی ایمیل')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
