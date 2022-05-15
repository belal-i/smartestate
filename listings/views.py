from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *
from config.models import Config
# Create your views here.

def list_rental(request):
    site_title = Config.objects.get_or_create()[0].site_title
    rental_listings = Listing.objects.filter(listing_type='rental')
    context = {
        'rental_listings': rental_listings,
        'site_title': site_title,
    }
    return render(request, 'listings/list-rental.html', context)

def list_for_sale(request):
    site_title = Config.objects.get_or_create()[0].site_title
    for_sale_listings = Listing.objects.filter(listing_type='for_sale')
    context = {
        'for_sale_listings': for_sale_listings,
        'site_title': site_title,
    }
    return render(request, 'listings/list-for-sale.html', context)

def list_redirect(request):
    return redirect('/')

def detail(request, listing_id):
    site_title = Config.objects.get_or_create()[0].site_title
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'site_title': site_title,
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)
