from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from listings.models import *
from broker.models import *
from broker.utils import *

from rest_framework import viewsets, permissions

from .serializers import *

def listings(request):
    if request.method == 'GET':
        listings = filter_search_listing(request.GET)
        serializer = ListingSerializer(listings, many=True)
        return JsonResponse(serializer.data, safe=False)
def seekings(request):
    if request.method == 'GET':
        seekings = filter_search_seeking(request.GET)
        serializer = SeekingSerializer(seekings, many=True)
        return JsonResponse(serializer.data, safe=False)
def matchings(request):
    if request.method == 'GET':
        matchings = Matching.objects.all()
        serializer = MatchingSerializer(matchings, many=True)
        return JsonResponse(serializer.data, safe=False)
