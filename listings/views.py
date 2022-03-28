from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *
from config.models import Config
# Create your views here.

def index(request):
    site_title = Config.objects.get_or_create(
        config_var="site_title")[0].config_val
    rental_listings = Listing.objects.filter(listing_type='rental')[:5]
    for_sale_listings = Listing.objects.filter(listing_type='for_sale')[:5]
    context = {
        'rental_listings': rental_listings,
        'for_sale_listings': for_sale_listings,
        'site_title': site_title,
    }
    return render(request, 'listings/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)
