from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist



from rest_framework import viewsets, permissions, status
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

from listings.models import *
from broker.models import *
from broker.utils import *
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


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def matchings(request):
    if request.method == 'GET':
        matchings = Matching.objects.all()
        serializer = MatchingSerializer(matchings, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        """
        To debug this, send a get request to server, get the CSRF token from
        that request, then paste it into a new  Header parameter called X-CSRFToken
        """
        listing_id = request.data.get('listing_id', '1')
        seeking_id = request.data.get('seeking_id', '1')
        error_occurred = False
        try:
            listing = Listing.objects.get(pk=listing_id)
            seeking = Seeking.objects.get(pk=seeking_id)
        except ObjectDoesNotExist:
            error_occurred = True
            error_response = {
                'status': 'Bad request',
                'message': 'Either the specified seeking or listing does not exist.',
            }

        if error_occurred:
            return JsonResponse(error_response,
                status=status.HTTP_400_BAD_REQUEST)
        else:
            matching = Matching(listing=listing, seeking=seeking)
            matching.save()

            serializer = MatchingSerializer(matching)
            return JsonResponse(serializer.data)
