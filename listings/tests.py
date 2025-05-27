from django.test import TestCase, RequestFactory

from .views import validate_search_params
from .functions import *


class TestSearch(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.maxDiff = None


    def test_validate_search_params(self):
        """
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
        test_url = "/listings/search?"
        # Empty value so that it gets popped from the return dict
        test_url += "listing_type=&"

        test_url += "max_rental_price=1000&"
        test_url += "min_rental_price=&"
        test_url += "max_security_deposit=3000&"
        test_url += "min_security_deposit=&"
        test_url += "max_for_sale_price=250000.0&"
        test_url += "min_for_sale_price=&"
        test_url += "min_minimum_down_payment=&"
        test_url += "max_minimum_down_payment=50000.0&"
        test_url += "earliest_date_available=&"
        test_url += "latest_date_available=1970-01-01&"
        test_url += "minimum_months=5&"
        test_url += "maximum_months=&"
        test_url += "max_number_of_people=&"
        test_url += "min_number_of_people=2&"
        test_url += "pets_ok=on&"
        test_url += "is_primary=on&"
        test_url += "max_number_of_rooms=&"
        test_url += "min_number_of_rooms=4&"
        test_url += "max_size_sq_m=&"
        test_url += "min_size_sq_m=40&"
        test_url += "has_internet=foobar&"
        test_url += "is_furnished=&"
        # We know that this isn't caught by validate_search_params;
        # It's caught in broker.utils.filter_search_listing
        test_url += "max_date_of_construction=foobar&"
        test_url += "min_date_of_construction=1970-01-01"
        test_request = self.factory.get(test_url)

        test_dict = {
            "max_rental_price": 1000.0,
            "max_security_deposit": 3000.0,
            "max_for_sale_price": 250000.0,
            "max_minimum_down_payment": 50000.0,
            "latest_date_available": "1970-01-01",
            "minimum_months": 5,
            "min_number_of_people": 2,
            "pets_ok": True,
            "is_primary": True,
            "min_number_of_rooms": 4,
            "min_size_sq_m": 40,
            # We know that this isn't caught by validate_search_params;
            # It's caught in broker.utils.filter_search_listing
            "max_date_of_construction": "foobar",
            "min_date_of_construction": "1970-01-01",
        }

        self.assertDictEqual(test_dict, validate_search_params(test_request.GET))
