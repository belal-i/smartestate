from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from listings.models import *
from broker.models import *
from broker.utils import *

from rest_framework import viewsets, permissions
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.decorators import (
    api_view, 
    authentication_classes,
    permission_classes,
)



from .serializers import *

"""
We want this to be readable by all. The search forms on the website actually
don't use this endpoint, they call broker.utils.filter_search_listing in
views of their own. However, in future versions, we probably want this
endpoint to be readable by all frontend users.
"""
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def listings(request):
    if request.method == 'GET':
        listings = filter_search_listing(request.GET)
        serializer = ListingSerializer(listings, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def seekings(request):
    if request.method == 'GET':
        seekings = filter_search_seeking(request.GET)
        serializer = SeekingSerializer(seekings, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def matchings(request):
    if request.method == 'GET':
        matchings = Matching.objects.all()
        serializer = MatchingSerializer(matchings, many=True)
        return JsonResponse(serializer.data, safe=False)
