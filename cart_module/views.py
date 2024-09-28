import sweetify
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from cart_module.models import Cart, CartDetail
from product_module.models import Product


# Create your views here.
def add_product_to_basket(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            cart, created = Cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
            cart_detail = cart.cartdetail_set.filter(product_id=product_id).first()
            if cart_detail is not None:
                cart_detail.count += count
                cart_detail.save()
                return JsonResponse({
                    'status': 'success',
                    'title': 'موفقیت آمیز',
                    'icon': 'success',
                    'text': 'محصول شما با موفقیت به سبد خرید اضافه شد',
                    'confirmButtonText': 'اوکی',
                    'persistent': True
                })

            else:
                new_cart = CartDetail(cart_id=cart.id, product_id=product_id, count=count)
                new_cart.save()
                return JsonResponse({
                    'status': 'success',
                    'title': 'موفقیت آمیز',
                    'icon': 'success',
                    'text': 'محصول شما با موفقیت وارد سبد خرید شد',
                    'confirmButtonText': 'اوکی',
                    'persistent': True
                })
        else:
            return JsonResponse({
                'status': 'no_product',
                'title': 'ناموفق',
                'icon': 'error',
                'text': 'محصول مورد نظر موجود نمی باشد',
                'confirmButtonText': 'اوکی',
                'persistent': True
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'title': 'اخطار',
            'icon': 'warning',
            'text': 'برای ثبت محصول ابتدا می بایست وارد سایت شوید',
            'confirmButtonText': 'اوکی',
            'persistent': True
        })
