from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard_page'),
    path('basket/', views.basket, name='cart_page'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_pass_page'),
    path('remove-product', views.remove_cart_detail, name='remove_product_from_basket'),
]
