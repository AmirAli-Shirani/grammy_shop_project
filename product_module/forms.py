from django import forms
from django.core.validators import MaxLengthValidator

from product_module.models import ProductComment


class ProductCommentForm(forms.Form):
    text = forms.Textarea(attrs={
        'class': 'form-control'
    })
