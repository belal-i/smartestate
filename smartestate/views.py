from django.http import HttpResponse
from django.shortcuts import render

from config.models import Config

def home(request):
    site_title = Config.objects.get_or_create()[0].site_title
    cover_text = Config.objects.get_or_create()[0].cover_text
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""
    return render(request, 'smartestate/home.html', {
        "site_title": site_title,
        "cover_text": cover_text,
        "logo_url": logo_url,
        }
    )
def about(request):
    site_title = Config.objects.get_or_create()[0].site_title
    about_text = Config.objects.get_or_create()[0].about_text
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""
    return render(request, 'smartestate/about.html', {
        "site_title": site_title,
        "about_text": about_text,
        "logo_url": logo_url,
        }
    )
