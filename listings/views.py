from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    rental_listings = Listing.objects.filter(listing_type='rental')[:5]
    for_sale_listings = Listing.objects.filter(listing_type='for_sale')[:5]
    context = {
        'rental_listings': rental_listings,
        'for_sale_listings': for_sale_listings,
    }
    return render(request, 'listings/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)
