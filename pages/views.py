from django.shortcuts import render, get_object_or_404, redirect

from .models import Page

# Create your views here.

def single_page(request, page_name):
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
