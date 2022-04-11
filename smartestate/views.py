from django.http import HttpResponse
from django.shortcuts import render
from config.models import Config

def home(request):
    site_title = Config.objects.get_or_create(
        config_var="site_title")[0].config_val
    cover_text = Config.objects.get(config_var="cover_text").config_val
    return render(request, 'smartestate/home.html', {
        "site_title": site_title,
        "cover_text": cover_text,
        }
    )
def about(request):
    site_title = Config.objects.get_or_create(
        config_var="site_title")[0].config_val
    about_text = Config.objects.get(config_var="about_text").config_val
    return render(request, 'smartestate/about.html', {
        "site_title": site_title,
        "about_text": about_text,
        }
    )
