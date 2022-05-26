from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from config.models import Config
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

def get_search_results(keyword):
    return Listing.objects.filter(
        Q(short_description__icontains = keyword) |
        Q(long_description__icontains = keyword) |
        Q(apartment__specials__icontains = keyword) |
        Q(apartment__house__real_estate__address__street__icontains =
            keyword) |
        Q(apartment__house__real_estate__address__city__icontains =
            keyword)
    )

def search_results(request):

    search_results = get_search_results(request.GET['search'])

    context = {
        'search_results': search_results,
    }
    return render(request, 'listings/search-results.html', context)
