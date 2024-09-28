from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View
from account_module.forms import LoginForm, RegisterForm, ForgetPasswordForm, ResetPasswordForm
from account_module.models import User
import sweetify
from utils.email_service import send_email


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_first_name = register_form.cleaned_data.get('first_name')
            user_last_name = register_form.cleaned_data.get('last_name')
            user_pass = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل مورد نظر قبلا ثبت نام کرده است')
            else:
                new_user = User(first_name=user_first_name, last_name=user_last_name, email=user_email, is_active=False,
                                email_active_code=get_random_string(72),
                                username=user_email)
                new_user.set_password(user_pass)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate-account.html')
                sweetify.sweetalert(self.request, title='اعلان', icon='warning', button='اوکی', persistent=True,
                                    text='شما با موفقیت ثبت نام شدید اما برای فعالسازی حساب کاربری و ورود به سایت باید روی لینکی که ما برای شما از طریق ایمیل ارسال کردیم کلیک کنید')
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    pass_is_correct = user.check_password(user_pass)
                    if pass_is_correct:
                        login(request, user)
                        sweetify.sweetalert(request, 'موفقیت آمیز', icon='success', button='اوکی', persistent=True,
                                            text='شما با موفقیت وارد شدید')
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'حساب کاربری با مشخصات فوق یافت نشد')
            else:
                login_form.add_error('email', 'حساب کاربری با مشخصات فوق یافت نشد')
        else:
            raise Http404()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ActivateAccountView(View):
    def get(self, request: HttpRequest, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(70)
                user.save()
                sweetify.sweetalert(self.request, title='موفقیت آمیز', icon='warning', button='اوکی',
                                    persistent=True,
                                    text='حساب کاربری شما با موفقیت فعال شد')
                return redirect(reverse('login_page'))
            else:
                sweetify.sweetalert(self.request, title='error', icon='error', button='اوکی', persistent=True,
                                    text='حساب کاربری شما قبلا فعال شده است')
        raise Http404()


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgetPasswordForm()
        context = {
            'forget_pass': forget_pass_form
        }
        return render(request, 'account_module/forget-pass.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'new_user': user}, 'emails/reset-pass.html')
                sweetify.sweetalert(self.request, title='اعلان', icon='success', button='اوکی', persistent=True,
                                    text='برای بازیابی رمز ورود بر روی لینکی که برای شما از طریق ایمیل ارسال کردیم کلیک کنید')

            else:
                forget_pass_form.add_error('email', 'کاربری با مشخصات فوق یافت نشد')
        context = {
            'forget_pass': forget_pass_form
        }
        return render(request, 'account_module/forget-pass.html', context)


@method_decorator(login_required, name='dispatch')
class ResetPasswordView(View):
    def get(self, request, active_code):
        reset_pass_form = ResetPasswordForm()
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        context = {
            'reset_pass': reset_pass_form
        }

        return render(request, 'account_module/reset-pass.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        if reset_pass_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                reset_pass_form.add_error('email', 'کاربری با مشخصات فوق یافت نشد')
            else:
                user_new_pass = reset_pass_form.cleaned_data.get('password')
                user.set_password(user_new_pass)
                user.is_active = True
                user.email_active_code = get_random_string(70)
                user.save()
                sweetify.sweetalert(self.request, title='اعلان', icon='success', button='اوکی', persistent=True,
                                    text='کلمه عبور شما با موفقیت تغییر پیدا کرد')
                return redirect(reverse('login_page'))
        context = {
            'reset_pass': reset_pass_form
        }
        return render(request, 'account_module/reset-pass.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))
