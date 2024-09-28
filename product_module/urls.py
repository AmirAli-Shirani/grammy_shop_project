from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductCatalogView.as_view(), name='product_catalog_page'),
    # path('shoes/<gender>/<category>/', views.ProductCategoryListView.as_view(), name='shoes_list_page'),
    path('shoes/<str:slug>', views.ProductDetailViewSecond.as_view(), name='shoes_detail_page'),
    path('category/<gender>/<category>/', views.ProductCategoryListView.as_view(), name='products_by_categories'),
    path('brand/<brand>/', views.ProductCategoryListView.as_view(), name='product_by_brands'),
    path('<str:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('favorites/', views.product_favourite_list, name='product_favorites'),
    path('add/<int:pk>/add', views.add_product, name='add_to_favorites'),
    path('remove/<int:pk>/remove', views.remove_product, name='remove_from_favorites')
]
