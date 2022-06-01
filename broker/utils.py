from django.db.models import Q
from listings.models import *
from .models import *

def keyword_search_listing(keyword):
    return Listing.objects.filter(
        Q(short_description__icontains = keyword) |
        Q(long_description__icontains = keyword) |
        Q(apartment__specials__icontains = keyword) |
        Q(apartment__house__real_estate__address__street__icontains =
            keyword) |
        Q(apartment__house__real_estate__address__city__icontains =
            keyword)
    )
def keyword_search_seeking(keyword):
    return Seeking.objects.filter(
        Q(contact__first_name__icontains = keyword) |
        Q(contact__last_name__icontains = keyword) |
        Q(contact__address__street__icontains = keyword) |
        Q(contact__address__city__icontains = keyword) |
        Q(occupation__icontains = keyword) |
        Q(employer__name__icontains = keyword) |
        Q(notes__icontains = keyword)
    )

def filter_search(params):
    pass
