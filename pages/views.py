from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation

from smartestate.settings import *
from smartestate.functions import tuple_list_has_key

from .models import Page

# Create your views here.

def single_page(request, page_name):
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
    # TODO: Maybe deal with this a little more gracefully, also,
    #       see Feature #340.
    try:
        page = get_object_or_404(Page, name=page_name)
    except:
        try:
            page = Page.objects.filter(name=page_name)[0]
        except:
            return redirect("/")

    return render(request, 'pages/single-page.html', {'page': page})
