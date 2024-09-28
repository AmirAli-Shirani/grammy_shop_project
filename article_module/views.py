from urllib import request

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.views.generic import ListView, TemplateView, DetailView

from article_module.models import Article, ArticleGallery, ArticleHeading
from product_module.models import ProductGallery, ProductCategory


# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_module/article-blog.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        # context['upper_articles'] = ArticleHeading.objects.all()
        return context


class ArticleDetailView(DetailView):
    template_name = 'article_module/article-single.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_products = self.object
        context['article_galleries'] = ArticleGallery.objects.filter(article_id=loaded_products.id).all()
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)[:6]
        return context
