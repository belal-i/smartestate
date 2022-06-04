from django.db.models import Q
from listings.models import *
from .models import *

def keyword_search_listing(keyword):
    return Listing.objects.filter(
        Q(short_description__icontains = keyword) |
        Q(long_description__icontains = keyword) |
        Q(apartment__specials__icontains = keyword) |
        Q(apartment__house__real_estate__address__street__icontains =
            keyword) |
        Q(apartment__house__real_estate__address__city__icontains =
            keyword)
    )
def keyword_search_seeking(keyword):
    return Seeking.objects.filter(
        Q(contact__first_name__icontains = keyword) |
        Q(contact__last_name__icontains = keyword) |
        Q(contact__address__street__icontains = keyword) |
        Q(contact__address__city__icontains = keyword) |
        Q(occupation__icontains = keyword) |
        Q(employer__name__icontains = keyword) |
        Q(notes__icontains = keyword)
    )

def filter_search_listing(params):
    """
    This function takes a dictionary of search parameters, and searches for 
    all listings in the database that meet the requirements.

    Some parameters are matched exactly, that is, they need to be equal, in
    order for the filter to return them.

    Others are matched on a greater-than- or less-than-or-equal basis.

    In some cases, whether it's less-than or greater-than, depends on the
    general business logic of real estate brokerage. We might refine this
    function to support lower and upper bounds for all those parameters.

    The function supports an input dictionary with the following keys:
    - listing_type
    - rental_price
    - security_deposit
    - for_sale_price
    - minimum_down_payment
    - earliest_date_available
    - latest_date_available
    - minimum_months
    - maximum_months
    - number_of_people
    - pets_ok
    - is_primary
    - number_of_rooms
    - size_sq_m
    - has_internet
    - is_furnished
    - date_of_construction
    """

    result = Listing.objects.all()
    try:
        result = result.filter(listing_type=params['listing_type'])
    except KeyError:
        pass
    try:
        result = result.filter(rental_price__lte=params['rental_price'])
    except KeyError:
        pass
    try:
        result = result.filter(
            security_deposit__lte=params['security_deposit']
        )
    except KeyError:
        pass
    try:
        result = result.filter(for_sale_price__lte=params['for_sale_price'])
    except KeyError:
        pass
    try:
        result = result.filter(
            minimum_down_payment__lte=params['minimum_down_payment']
        )
    except KeyError:
        pass
    try:
        result = result.filter(date_available__gte=params['earliest_date_available'])
    except KeyError:
        pass
    try:
        result = result.filter(date_available__lte=params['latest_date_available'])
    except KeyError:
        pass
    try:
        result = result.filter(minimum_months__gte=params['minimum_months'])
    except KeyError:
        pass
    try:
        result = result.filter(maximum_months__lte=params['maximum_months'])
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_people__lte=params['number_of_people']
        )
    except KeyError:
        pass
    try:
        result = result.filter(pets_ok=params['pets_ok'])
    except KeyError:
        pass
    try:
        result = result.filter(apartment__is_primary=params['is_primary'])
    except KeyError:
        pass
    try:
        result = result.filter(
            apartment__number_of_rooms__gte=params['number_of_rooms']
        )
    except KeyError:
        pass
    try:
        result = result.filter(apartment__size_sq_m__gte=params['size_sq_m'])
    except KeyError:
        pass
    try:
        result = result.filter(apartment__has_internet=params['has_internet'])
    except KeyError:
        pass
    try:
        result = result.filter(apartment__is_furnished=params['is_furnished'])
    except KeyError:
        pass
    try:
        result = result.filter(
            apartment__house__date_of_construction__gte=params[
                'date_of_construction']
            )
    except KeyError:
        pass

    return result


def filter_search_seeking(params):
    pass
def filter_search_matching(params):
    pass
