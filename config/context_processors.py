from .models import Config

def site_title(request):
    site_title = Config.objects.get_or_create()[0].site_title
    if site_title is None:
        site_title = ""
    return {'site_title': site_title}
def logo_url(request):
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""
    return {'logo_url': logo_url}

def theme(request):
    return {'theme': Config.objects.get_or_create()[0].theme}

def show_filter_search_on_homepage(request):
    return {
        'show_filter_search_on_homepage': \
            Config.objects.get_or_create()[0].show_filter_search_on_homepage
    }
def show_filter_search_in_listview(request):
    return {
        'show_filter_search_in_listview': \
            Config.objects.get_or_create()[0].show_filter_search_in_listview
    }
