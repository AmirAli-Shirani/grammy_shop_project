from django.contrib import admin

from article_module import models
from article_module.models import Article, ArticleGallery, ArticleHeading


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_active']
    prepopulated_fields = {'slug': ['title'], }

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(models.ArticleGallery)

@admin.register(ArticleHeading)
class ArticleHeadingAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_active']
    prepopulated_fields = {'slug': ['title'], }

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)