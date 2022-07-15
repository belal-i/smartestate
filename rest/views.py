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


@api_view(['GET', 'POST', 'PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def matchings(request):
    if request.method == 'GET':
        matchings = filter_search_matching(request.GET)
        serializer = MatchingSerializer(matchings, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        """
        To debug this, send a get request to server, get the CSRF token from
        that request, then paste it into a new  Header parameter called X-CSRFToken
        """
        listing_id = request.data.get('listing_id', '1')
        seeking_id = request.data.get('seeking_id', '1')
        try:
            listing = Listing.objects.get(pk=listing_id)
            seeking = Seeking.objects.get(pk=seeking_id)
        except ObjectDoesNotExist:
            error_response = {
                'status': 'Not found',
                'message': 'Either the specified seeking or listing does not exist.',
            }
            return JsonResponse(error_response,
                status=status.HTTP_404_NOT_FOUND)

        matching = Matching(listing=listing, seeking=seeking)
        matching.save()

        serializer = MatchingSerializer(matching)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':

        matching_id = request.data.get('id')

        try:
            matching = Matching.objects.get(pk=matching_id)
        except ObjectDoesNotExist:
            error_response = {
                "status": "Not found",
                "message": "The specified matching does not exist.",
            }
            return JsonResponse(error_response,
                status=status.HTTP_404_NOT_FOUND)

        """
        See Feature #399: At the moment, we only really care about the status,
        but we would probably also want to change the listing_id and
        seeking_id via PATCH request soon.
        """
        try:
            matching.status = request.data.get('status')
        except:
            error_response = {
                "status": "Bad request",
                "message": "Could not set the matching's status.",
            }
            return JsonResponse(error_response,
                status=status.HTTP_400_BAD_REQUEST)

        try:
            matching.note = request.data.get('note')
        except:
            error_response = {
                "status": "Bad request",
                "message": "Could not set the matching's note.",
            }
            return JsonResponse(error_response,
                status=status.HTTP_400_BAD_REQUEST)

        matching.save()
        serializer = MatchingSerializer(matching)
        return JsonResponse(serializer.data)
