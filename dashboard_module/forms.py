from django.core.exceptions import ValidationError
from django import forms


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label=': رمز فعلی',
        widget=forms.PasswordInput(attrs={
            'style': 'height:50px; margin-bottom:20px;', 'class': 'form-control text-right',
            'placeholder': 'current password'
        })
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
