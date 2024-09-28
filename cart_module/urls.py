from django.urls import path

from . import views

urlpatterns = [
    path('add-to-basket', views.add_product_to_basket, name='add_to_basket')
]
