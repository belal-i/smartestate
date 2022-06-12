from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from listings.models import *
from broker.models import *

from rest_framework import viewsets, permissions

from .serializers import *

def listings(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return JsonResponse(serializer.data, safe=False)
def seekings(request):
    if request.method == 'GET':
        seekings = Seeking.objects.all()
        serializer = SeekingSerializer(seekings, many=True)
        return JsonResponse(serializer.data, safe=False)
def matchings(request):
    if request.method == 'GET':
        matchings = Matching.objects.all()
        serializer = MatchingSerializer(matchings, many=True)
        return JsonResponse(serializer.data, safe=False)
