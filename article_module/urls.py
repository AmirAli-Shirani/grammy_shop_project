from django.urls import path

from article_module import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_page'),
    path('<pk>', views.ArticleDetailView.as_view(), name='article_detail_page')
]
