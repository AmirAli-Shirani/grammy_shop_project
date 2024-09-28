from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.models import ProductCategory, Product, Shoes, ShoesCategory
from site_module.models import SiteBanner, SiteSliders


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['latest_products'] = Product.objects.filter(is_active=True, is_delete=False).order_by('-create_date')[
                                     :10]
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)
        context['site_banners_upside'] = SiteBanner.objects.filter(is_active=True,
                                                                   position__iexact=SiteBanner.SiteBannerChoices.home_page_upside)
        context['site_sliders'] = SiteSliders.objects.filter(is_active=True)
        context['site_banners_downside'] = SiteBanner.objects.filter(is_active=True,
                                                                     position__iexact=SiteBanner.SiteBannerChoices.home_page_downside)
        # context['latest_shoes'] = Shoes.objects.filter(is_active=True, is_delete=False).order_by('-id')[:10]
        context['most_visited_products'] = Product.objects.filter(is_active=True).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:10]
        return context


class SiteHeaderComponents(TemplateView):
    template_name = 'shared/header-components.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product_categories_women'] = ProductCategory.objects.filter(is_delete=False, is_active=True,
                                                                             gender__url_title__iexact='women')
        context['product_categories_men'] = ProductCategory.objects.filter(is_delete=False, is_active=True,
                                                                           gender__url_title__iexact='men')
        context['shoes_categories'] = ShoesCategory.objects.filter(is_active=True)
        return context


class SiteFooterComponents(TemplateView):
    template_name = 'shared/footer-components.html'
