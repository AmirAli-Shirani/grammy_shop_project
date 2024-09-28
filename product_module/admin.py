from django.contrib import admin
from product_module.models import ProductBrand, Product, ProductCategory, ProductGallery, Person, Shoes, ShoesCategory, \
    ProductComment


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'parents','id', 'brand', 'is_active', 'is_delete')
    prepopulated_fields = {'slug': ['title']}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['url_title']


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['title','id', 'category', 'is_active']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ShoesCategory)
class ShoesCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'is_active']


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product','shoes', 'user', 'parent']
