# Create your views here.
import sweetify
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from product_module.models import ProductCategory, Product, Person, ProductBrand, ShoesCategory, Shoes, \
    ProductComment, ProductVisit
from site_module.models import SiteBanner
from utils.http_service import get_client_ip


class ProductCatalogView(TemplateView):
    template_name = 'product_module/product-catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories_women_gender'] = ProductCategory.objects.filter(is_active=True, is_delete=False,
                                                                            gender__url_title__iexact='women')
        context['categories_men_gender'] = ProductCategory.objects.filter(is_active=True, is_delete=False,
                                                                          gender__url_title__iexact='men')
        context['women_picture'] = Person.objects.get(url_title__iexact='women')
        context['men_picture'] = Person.objects.get(url_title__iexact='men')
        context['shoes_categories_women'] = ShoesCategory.objects.filter(is_active=True, is_delete=False,
                                                                         gender__url_title__iexact='women')
        context['shoes_categories_men'] = ShoesCategory.objects.filter(is_active=True, is_delete=False,
                                                                       gender__url_title__iexact='men')
        return context


class ProductCategoryListView(ListView):
    template_name = 'product_module/product-list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(*args, **kwargs)
        gender_name = self.kwargs.get('gender')
        cat_name = self.kwargs.get('category')
        context['product_cat'] = ProductCategory.objects.filter(is_delete=False, is_active=True,
                                                                url_title__iexact=cat_name).first()
        context['product_brand'] = ProductBrand.objects.filter(is_active=True)
        context['site_banners'] = SiteBanner.objects.filter(is_active=True,
                                                            position__iexact=SiteBanner.SiteBannerChoices.product_list)
        context['shoes_products'] = Shoes.objects.filter(is_active=True, is_delete=False,
                                                         category__gender__url_title__iexact=gender_name,
                                                         category__url_title__iexact=cat_name)
        return context

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True, is_delete=False)
        category_name = self.kwargs.get('category')
        gender_name = self.kwargs.get('gender')
        brand_name = self.kwargs.get('brand')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if gender_name is not None:
            query = query.filter(category__gender__url_title__iexact=gender_name)
        if brand_name is not None:
            query = query.filter(brand__slug__iexact=brand_name)
        return query



class ProductDetailView(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_products = self.object
        request = self.request
        context['latest_products'] = Product.objects.filter(is_active=True, is_delete=False).order_by('-create_date')[
                                     :10]
        context['related_products'] = Product.objects.filter(is_active=True, is_delete=False,
                                                             brand__product=loaded_products.id).exclude(
            id=loaded_products.id)[:4]
        context['site_banners_detail'] = SiteBanner.objects.filter(is_active=True,
                                                                   position__iexact=SiteBanner.SiteBannerChoices.product_detail)
        product: Product = kwargs.get('object')
        context['comments'] = ProductComment.objects.filter(parent=None, product_id=product).prefetch_related(
            'productcomment_set')
        is_favorite = False
        if product.favorite.filter(id=request.user.id).exists():
            is_favorite = True
            context['is_favorite'] = is_favorite
        user_ip = get_client_ip(self.request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_products.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_products.id)
            new_visit.save()
        return context


class ProductDetailViewSecond(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Shoes

    def get_context_data(self, *args, **kwargs, ):
        context = super().get_context_data()
        loaded_products = self.object
        request = self.request
        context['latest_shoes'] = Shoes.objects.filter(is_active=True, is_delete=False).order_by('-create_date')[
                                  :10]
        context['related_shoes'] = Shoes.objects.filter(is_active=True, is_delete=False,
                                                        brand__shoes=loaded_products.id).exclude(id=loaded_products.id)[
                                   :4]
        context['site_banners_detail'] = SiteBanner.objects.filter(is_active=True,
                                                                   position__iexact=SiteBanner.SiteBannerChoices.product_detail)
        shoes: Shoes = kwargs.get('object')
        context['comments'] = ProductComment.objects.filter(parent=None, shoes_id=shoes).prefetch_related(
            'productcomment_set')
        is_favorite = False
        if shoes.favorite.filter(id=request.user.id).exists():
            is_favorite = True
            context['is_favorite'] = is_favorite
        return context


def product_by_categories(request: HttpRequest):
    product_category = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_category,
    }
    return render(request, 'product_module/components/product-categories.html', context)


def product_by_brands(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product-brand-copmonent.html', context)


def shoes_by_categories(request: HttpRequest):
    shoes_categories = ShoesCategory.objects.filter(is_active=True)
    context = {
        'shoes': shoes_categories
    }
    return render(request, 'product_module/components/shoes-categories-components.html', context)


def product_favourite_list(request):
    user = request.user
    favourite_products = user.product_favorites.all()
    fav_products = user.shoes_favorites.all()

    context = {
        'favorite_products': favourite_products,
        'fav_products': fav_products
    }
    return render(request, 'product_module/product_favorites.html', context)


def add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user not in product.favorite.all():
        product.favorite.add(request.user)
        sweetify.sweetalert(request, title='اعلان', icon='success', persistent=True, button='اوکی',
                            text='محصول شما با موفقیت به سبد خرید اضافه شد')
    shoes = get_object_or_404(Shoes, pk=pk)
    if shoes:
        if request.user not in shoes.favorite.all():
            shoes.favorite.add(request.user)
            sweetify.sweetalert(request, title='اعلان', icon='success', persistent=True, button='اوکی',
                                text='محصول شما با موفقیت به سبد خرید اضافه شد')

    return HttpResponseRedirect(reverse('product_favorites'))


def remove_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user in product.favorite.all():
        product.favorite.remove(request.user)
        sweetify.sweetalert(request, title='اعلان', icon='success', persistent=True, button='اوکی',
                            text='محصول شما با موفقیت از سبد خرید حذف شد')
    else:
        shoes = get_object_or_404(Shoes, pk=pk)
        if request.user in shoes.favorite.all():
            shoes.favorite.remove(request.user)
            sweetify.sweetalert(request, title='اعلان', icon='success', persistent=True, button='اوکی',
                                text='محصول شما با موفقیت از سبد خرید حذف شد')
    return HttpResponseRedirect(reverse('product_favorites'))
