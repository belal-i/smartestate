from django.shortcuts import render
from django.http import HttpResponse

from listings.models import *
from .models import *

# Create your views here.

def start(request):
    listings = Listing.objects.all()[:10]
    seekings = Seeking.objects.all()[:10]
    matchings = Matching.objects.all()[:10]
    context = {
        'listings': listings,
        'seekings': seekings,
        'matchings': matchings,
    }
    return render(request, 'broker/start.html', context)
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'broker/listings.html', {'listings': listings})
def seekings(request):
    seekings = Seeking.objects.all()
    return render(request, 'broker/seekings.html', {'seekings': seekings})
def matchings(request):
    matchings = Matching.objects.all()
    return render(request, 'broker/matchings.html', {'matchings': matchings})
