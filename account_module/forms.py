from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, EmailValidator


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label=': نام',
        widget=forms.TextInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'Name'
        })
    )
    last_name = forms.CharField(
        label=': نام خانوادگی',
        widget=forms.TextInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'LastName'
        })
    )
    email = forms.EmailField(
        label=': ایمیل',
        widget=forms.EmailInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'email'
        }),
        validators=[MaxLengthValidator(100), validators.EmailValidator]
    )

    password = forms.CharField(
        label=': کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'password'
        })
    )
    confirm_password = forms.CharField(
        label=': تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'confirm-password'
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور و تکرار آن مغایرت ندارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label=': ایمیل',
        widget=forms.EmailInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'email'
        }),
        validators=[MaxLengthValidator(100), validators.EmailValidator]
    )

    password = forms.CharField(
        label=': کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'password'
        }),
        validators=[MaxLengthValidator(100)]
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label=': ایمیل',
        widget=forms.EmailInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'email'
        }),
        validators=[MaxLengthValidator(100), validators.EmailValidator]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label=': کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'password'
        })
    )
    confirm_password = forms.CharField(
        label=': تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'confirm-password'
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور و تکرار آن مغایرت ندارند')
