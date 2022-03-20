from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Listing
# Create your views here.

def index(request):
    latest_listings = Listing.objects.all()[:5]
    context = {
        'latest_listings': latest_listings,
    }
    return render(request, 'listings/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)

