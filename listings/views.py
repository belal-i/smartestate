from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from config.models import Config
from broker.utils import keyword_search_listing
# Create your views here.

def list_rental(request):

    rental_listings = Listing.objects.filter(listing_type='rental')
    context = {
        'rental_listings': rental_listings,
    }
    return render(request, 'listings/list-rental.html', context)

def list_for_sale(request):

    for_sale_listings = Listing.objects.filter(listing_type='for_sale')
    context = {
        'for_sale_listings': for_sale_listings,
    }
    return render(request, 'listings/list-for-sale.html', context)

def list_redirect(request):
    return redirect('/')

def detail(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)

def search_results(request):

    search_results = keyword_search_listing(request.GET['search'])

    context = {
        'search_results': search_results,
    }
    return render(request, 'listings/search-results.html', context)
