from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.utils import translation
from smartestate.settings import *
from smartestate.functions import tuple_list_has_key
from config.models import Config
from broker.utils import keyword_search_listing, filter_search_listing
from .models import *
from .functions import *


def list_rental(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    rental_listings = Listing.objects.filter(listing_type='rental')
    context = {
        'rental_listings': rental_listings,
    }
    return render(request, 'listings/list-rental.html', context)


def list_for_sale(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    for_sale_listings = Listing.objects.filter(listing_type='for_sale')
    context = {
        'for_sale_listings': for_sale_listings,
    }
    return render(request, 'listings/list-for-sale.html', context)


def list_redirect(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    return redirect('/')


def detail(request, listing_id):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context)


def search_results(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')

    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    if request.GET.get('search', '') != '':
        search_results = keyword_search_listing(request.GET['search'])
    else:
        search_results = filter_search_listing(
            validate_search_params(request.GET)
        )

    context = {
        'search_results': search_results,
    }

    return render(request, 'listings/search-results.html', context)
