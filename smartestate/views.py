from django.http import HttpResponse
from django.shortcuts import render

from config.models import Config

def home(request):
    cover_text = Config.objects.get_or_create()[0].cover_text
    return render(request, 'smartestate/home.html', {
        "cover_text": cover_text,
        }
    )
