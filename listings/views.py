from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from config.models import Config
# Create your views here.

def list_rental(request):
    site_title = Config.objects.get_or_create()[0].site_title
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""

    rental_listings = Listing.objects.filter(listing_type='rental')
    context = {
        'rental_listings': rental_listings,
        'site_title': site_title,
        'logo_url': logo_url,
    }
    return render(request, 'listings/list-rental.html', context)

def list_for_sale(request):
    site_title = Config.objects.get_or_create()[0].site_title
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""

    for_sale_listings = Listing.objects.filter(listing_type='for_sale')
    context = {
        'for_sale_listings': for_sale_listings,
        'site_title': site_title,
        'logo_url': logo_url,
    }
    return render(request, 'listings/list-for-sale.html', context)

def list_redirect(request):
    return redirect('/')

def detail(request, listing_id):
    site_title = Config.objects.get_or_create()[0].site_title
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'site_title': site_title,
        'listing': listing,
        'logo_url': logo_url,
    }
    return render(request, 'listings/detail.html', context)

def get_search_results(keyword):
    return Listing.objects.filter(
        Q(short_description__contains = keyword) |
        Q(long_description__contains = keyword) |
        Q(apartment__specials__contains = keyword) |
        Q(apartment__house__real_estate__address__street__contains =
            keyword) |
        Q(apartment__house__real_estate__address__city__contains =
            keyword)
    )

def search_results(request):
    site_title = Config.objects.get_or_create()[0].site_title
    try:
        logo_url   = Config.objects.get_or_create()[0].logo_image.url
    except ValueError:
        logo_url   = ""

    search_results = get_search_results(request.GET['search'])

    context = {
        'search_results': search_results,
        'site_title': site_title,
        'logo_url': logo_url,
    }
    return render(request, 'listings/search-results.html', context)
