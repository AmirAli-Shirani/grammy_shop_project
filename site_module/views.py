from django.shortcuts import render
from django.views.generic import TemplateView

from account_module.models import User


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'site_module/about-us.html'