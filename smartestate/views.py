from django.http import HttpResponse
from django.shortcuts import render
from config.models import Config

def index(request):
    site_title = Config.objects.get_or_create(
        config_var="site_title")[0].config_val
    return render(request, 'index.html', {"site_title": site_title})
