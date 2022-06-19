from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from config.models import Config
from broker.utils import keyword_search_listing, filter_search_listing
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

def search_results(request):

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

def validate_search_params(input_dict):
    return_dict = input_dict.copy().dict()
    str_fields = [
        'listing_type',
        'earliest_date_available',
        'latest_date_available',
        'max_date_of_construction',
        'min_date_of_construction',
    ]
    bool_fields = [
        'pets_ok',
        'is_primary',
        'has_internet',
        'is_furnished',
    ]
    int_fields = [
        'minimum_months',
        'maximum_months',
        'max_number_of_people',
        'min_number_of_people',
        'max_number_of_rooms',
        'min_number_of_rooms',
        'max_size_sq_m',
        'min_size_sq_m',
    ]
    float_fields = [
        'max_rental_price',
        'min_rental_price',
        'max_security_deposit',
        'min_security_deposit',
        'max_for_sale_price',
        'min_for_sale_price',
        'min_minimum_down_payment',
        'max_minimum_down_payment',
    ]
    for field in str_fields:
        try:
            if return_dict[field] == '':
                return_dict.pop(field)
        except KeyError:
            pass
    for field in bool_fields:
        try:
            if return_dict[field] == "on":
                return_dict[field] = True
        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)
    for field in int_fields:
        try:
            return_dict[field] = int(return_dict[field])
        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)
    for field in float_fields:
        try:
            return_dict[field] = float(return_dict[field])
        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)
    return return_dict
