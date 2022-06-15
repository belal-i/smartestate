import datetime

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

    The function supports an input dictionary with the following keys:
    - listing_type
    - max_rental_price
    - min_rental_price
    - max_security_deposit
    - min_security_deposit
    - max_for_sale_price
    - min_for_sale_price
    - min_minimum_down_payment
    - max_minimum_down_payment
    - earliest_date_available
    - latest_date_available
    - minimum_months
    - maximum_months
    - max_number_of_people
    - min_number_of_people
    - pets_ok
    - is_primary
    - max_number_of_rooms
    - min_number_of_rooms
    - max_size_sq_m
    - min_size_sq_m
    - has_internet
    - is_furnished
    - max_date_of_construction
    - min_date_of_construction
    """

    result = Listing.objects.all()
    try:
        result = result.filter(listing_type=params['listing_type'])
    except KeyError:
        pass
    try:
        result = result.filter(rental_price__lte=params['max_rental_price'])
    except KeyError:
        pass
    try:
        result = result.filter(rental_price__gte=params['min_rental_price'])
    except KeyError:
        pass
    try:
        result = result.filter(
            security_deposit__lte=params['max_security_deposit']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            security_deposit__gte=params['min_security_deposit']
        )
    except KeyError:
        pass
    try:
        result = result.filter(for_sale_price__lte=params['max_for_sale_price'])
    except KeyError:
        pass
    try:
        result = result.filter(for_sale_price__gte=params['min_for_sale_price'])
    except KeyError:
        pass
    try:
        result = result.filter(
            minimum_down_payment__lte=params['max_minimum_down_payment']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            minimum_down_payment__gte=params['min_minimum_down_payment']
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
            number_of_people__lte=params['max_number_of_people']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_people__gte=params['min_number_of_people']
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
            apartment__number_of_rooms__gte=params['min_number_of_rooms']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            apartment__number_of_rooms__lte=params['max_number_of_rooms']
        )
    except KeyError:
        pass
    try:
        result = result.filter(apartment__size_sq_m__gte=params['min_size_sq_m'])
    except KeyError:
        pass
    try:
        result = result.filter(apartment__size_sq_m__lte=params['max_size_sq_m'])
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
                'min_date_of_construction']
            )
    except KeyError:
        pass
    try:
        result = result.filter(
            apartment__house__date_of_construction__lte=params[
                'max_date_of_construction']
            )
    except KeyError:
        pass

    return result


def filter_search_seeking(params):
    """
    This function takes a dictionary of search parameters, and searches for 
    all seekings in the database that meet the requirements.

    Some parameters are matched exactly, that is, they need to be equal, in
    order for the filter to return them.

    Others are matched on a greater-than- or less-than-or-equal basis.

    The function supports an input dictionary with the following keys:
    - seeking_type
    - max_rent
    - min_rent
    - max_purchase_price
    - min_purchase_price
    - min_number_of_rooms
    - max_number_of_rooms
    - min_size_sq_m
    - max_size_sq_m
    - min_number_of_persons
    - max_number_of_persons
    - min_starting_date
    - max_starting_date
    - min_ending_date
    - max_ending_date
    - min_number_of_months
    - max_number_of_months
    - must_be_furnished
    - must_have_internet
    - is_smoker
    - has_pets
    - min_age (derived from seeking.contact.date_of_birth)
    - max_age (derived from seeking.contact.date_of_birth)
    """

    result = Seeking.objects.all()
    try:
        result = result.filter(seeking_type=params['seeking_type'])
    except KeyError:
        pass
    try:
        result = result.filter(max_rent__lte=params['max_rent'])
    except KeyError:
        pass
    try:
        result = result.filter(max_rent__gte=params['min_rent'])
    except KeyError:
        pass
    try:
        result = result.filter(
            max_purchase_price__lte=params['max_purchase_price']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            max_purchase_price__gte=params['min_purchase_price']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            min_number_of_rooms__gte=params['min_number_of_rooms']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            min_number_of_rooms__lte=params['max_number_of_rooms']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            min_size_sq_m__gte=params['min_size_sq_m']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            min_size_sq_m__lte=params['max_size_sq_m']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_persons__gte=params['min_number_of_persons']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_persons__lte=params['max_number_of_persons']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            starting_date__gte=params['min_starting_date']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            starting_date__lte=params['max_starting_date']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            ending_date__gte=params['min_ending_date']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            ending_date__lte=params['max_ending_date']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_months__gte=params['min_number_of_months']
        )
    except KeyError:
        pass
    try:
        result = result.filter(
            number_of_months__lte=params['max_number_of_months']
        )
    except KeyError:
        pass
    try:
        result = result.filter(must_be_furnished=params['must_be_furnished'])
    except KeyError:
        pass
    try:
        result = result.filter(must_have_internet=params['must_have_internet'])
    except KeyError:
        pass
    try:
        result = result.filter(is_smoker=params['is_smoker'])
    except KeyError:
        pass
    try:
        result = result.filter(has_pets=params['has_pets'])
    except KeyError:
        pass
    try:
        today = datetime.date.today()
        max_y_of_birth = today.year - params['min_age']
        max_dob = str(max_y_of_birth) + "-" + str(today.month) + "-" + \
            str(today.day)
        result = result.filter(contact__date_of_birth__lte=max_dob)
    except KeyError:
        pass
    try:
        today = datetime.date.today()
        min_y_of_birth = today.year - params['max_age']
        min_dob = str(min_y_of_birth) + "-" + str(today.month) + "-" + \
            str(today.day)
        result = result.filter(contact__date_of_birth__gte=min_dob)
    except KeyError:
        pass

    return result


def filter_search_matching(params):
    pass
