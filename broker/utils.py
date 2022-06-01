from django.db.models import Q
from listings.models import *

def keyword_search(keyword):
    return Listing.objects.filter(
        Q(short_description__icontains = keyword) |
        Q(long_description__icontains = keyword) |
        Q(apartment__specials__icontains = keyword) |
        Q(apartment__house__real_estate__address__street__icontains =
            keyword) |
        Q(apartment__house__real_estate__address__city__icontains =
            keyword)
    )

def filter_search(params):
    pass
