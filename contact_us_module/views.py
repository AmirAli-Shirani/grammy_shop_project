from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from contact_us_module.forms import ContactUsModelForm


# Create your views here.
class ContactUsView(CreateView):
    template_name = 'contact_us_module/contact-us.html'
    form_class = ContactUsModelForm
    success_url = '/products/'
