from django.http import HttpResponse
from django.shortcuts import render
from config.models import Config
from config.populate import populate

# TODO: A more Django native way to do this?
populate()

def index(request):
    site_title = Config.objects.get(config_var="site_title").config_val
    cover_text = Config.objects.get(config_var="cover_text").config_val
    return render(request, 'index.html', {
        "site_title": site_title,
        "cover_text": cover_text,
        }
    )
def about(request):
    site_title = Config.objects.get(config_var="site_title").config_val
    # TODO: In terms of type safety, it might be better to do it like this,
    # with .filter instead of .get
    about_text = Config.objects.filter(config_var="about_text")[0].config_val
    return render(request, 'about.html', {
        "site_title": site_title,
        "about_text": about_text,
        }
    )
