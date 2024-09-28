from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from cart_module.models import Cart
from dashboard_module.forms import ChangePasswordForm


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard_module/dashboard.html'


@login_required
def panel_dashboard(request):
    return render(request, 'dashboard_module/components/list-group.html')


def basket(request: HttpRequest):
    cart, created = Cart.objects.prefetch_related('cartdetail_set').get_or_create(is_paid=False,
                                                                                  user_id=request.user.id)
    total_amount = 0
    for cart_detail in cart.cartdetail_set.all():
        total_amount += cart_detail.count * cart_detail.product.price

    context = {
        'cart': cart,
        'sum': total_amount
    }
    return render(request, 'dashboard_module/cart.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        change_pass = ChangePasswordForm()
        context = {
            'change_pass': change_pass
        }
        return render(request, 'dashboard_module/change-pass.html', context)

    def post(self, request: HttpRequest):
        change_pass = ChangePasswordForm(request.POST)
        if change_pass.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(change_pass.cleaned_data.get('current_password')):
                current_user.set_password('password')
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                change_pass.add_error('current_password', 'کلمه عبور وارد شده اشتباه است')
        context = {
            'change_pass': change_pass
        }
        return render(request, 'dashboard_module/change-pass.html', context)


def remove_cart_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'detail_id_not_found'
        })
    cart, created = Cart.objects.prefetch_related('cartdetail_set').get_or_create(is_paid=False,
                                                                                  user_id=request.user.id)
    detail = cart.cartdetail_set.filter(id=detail_id).first()
    if detail is None:
        return JsonResponse({
            'status': 'no_detail_found'
        })
    detail.delete()
    cart, created = Cart.objects.prefetch_related('cartdetail_set').get_or_create(is_paid=False,
                                                                                  user_id=request.user.id)
    total_amount = 0
    for cart_detail in cart.cartdetail_set.all():
        total_amount += cart_detail.count * cart_detail.product.price

    context = {
        'cart': cart,
        'sum': total_amount
    }
    data = render_to_string('dashboard_module/cart.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })
