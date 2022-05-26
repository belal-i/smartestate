from .models import Page

def all_pages(request):
    all_pages = Page.objects.all().order_by('position')
    return {'all_pages': all_pages}
