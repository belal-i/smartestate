from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *
from config.models import Config
# Create your views here.

def list(request):
    site_title = Config.objects.filter(
        config_var="site_title")[0].config_val
    rental_listings = Listing.objects.filter(listing_type='rental')[:5]
    for_sale_listings = Listing.objects.filter(listing_type='for_sale')[:5]
    context = {
        'rental_listings': rental_listings,
        'for_sale_listings': for_sale_listings,
        'site_title': site_title,
    }
    return render(request, 'listings/list.html', context)

def detail(request, listing_id):
    site_title = Config.objects.filter(
        config_var="site_title")[0].config_val
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'site_title': site_title,
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)
