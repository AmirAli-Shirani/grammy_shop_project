from django.contrib import admin
from .models import SiteBanner
from . import models


# Register your models here.
@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position', 'is_active']


admin.site.register(models.SiteSliders)
