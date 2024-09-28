from django import forms

from contact_us_module.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'عنوان',
                'style': 'height: 4rem '
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'نام و نام خانوادگی',
                'style': 'height: 4rem '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control text-right',
                'placeholder': 'ایمیل',
                'style': 'height: 4rem '
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control text-right',
                'placeholder': 'پیام'
            })
        }
        labels = {
            'title': 'عنوان پیام',
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'message': 'پیام',
        }
        error_messages = {
            'full_name': {
                'required': 'نامو نام خانوادگی اجباری می باشد لطفا وارد نمایید'
            },
            'email': {
                'required': 'لطفا ایمیل خود را درست وارد نمایید'
            },
            'title': {
                'required': 'لطفا عنوان خود را درست وارد نمایید'
            },
            'message': {
                'required': 'لطفا متن پیام خود را درست وارد نمایید'
            },
        }