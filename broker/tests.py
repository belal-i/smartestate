from django.test import TestCase

from .utils import *
from listings.models import *
from .models import *

# Create your tests here.

class TestSearch(TestCase):
    def test_keyword_search_listing(self):
        test_address = Address(street="hello", city="world", pk=1)
        test_real_estate = RealEstate(address=test_address, pk=1)
        test_house = House(real_estate=test_real_estate, pk=1)
        test_apartment = Apartment(specials="test", house=test_house, pk=1)
        test_listing = Listing(
            short_description="foo",
            long_description="bar",
            apartment=test_apartment,
            pk=1
        )
        test_address.save()
        test_real_estate.save()
        test_house.save()
        test_apartment.save()
        test_listing.save()

        test_query_set = Listing.objects.filter(pk=1)

        test_search_1 = keyword_search_listing("Hello")
        test_search_2 = keyword_search_listing("World")
        test_search_3 = keyword_search_listing("Test")
        test_search_4 = keyword_search_listing("Foo")
        test_search_5 = keyword_search_listing("Bar")
        test_search_6 = keyword_search_listing("Boo")

        self.assertQuerysetEqual(test_query_set, test_search_1)
        self.assertQuerysetEqual(test_query_set, test_search_2)
        self.assertQuerysetEqual(test_query_set, test_search_3)
        self.assertQuerysetEqual(test_query_set, test_search_4)
        self.assertQuerysetEqual(test_query_set, test_search_5)
        self.assertEqual(test_search_6.count(), 0)

    def test_keyword_search_seeking(self):
        test_address = Address(street="Hello", city="World", pk=1)
        test_address.save()

        test_contact = Contact(first_name="John", last_name="Doe", pk=1)
        test_contact.save()
        test_contact.address.add(test_address)

        test_employer = Company(name="Acme", pk=1)
        test_employer.save()

        test_seeking = Seeking(contact=test_contact, pk=1, occupation="Foo",
            employer=test_employer,
            notes="The quick brown fox jumps over the lazy dog.")
        test_seeking.save()

        test_query_set = Seeking.objects.filter(pk=1)

        test_search_1 = keyword_search_seeking("hello")
        test_search_2 = keyword_search_seeking("world")
        test_search_3 = keyword_search_seeking("john")
        test_search_4 = keyword_search_seeking("doe")
        test_search_5 = keyword_search_seeking("dow")
        test_search_6 = keyword_search_seeking("foo")
        test_search_7 = keyword_search_seeking("acme")
        test_search_8 = keyword_search_seeking("lazy DOG")

        self.assertQuerysetEqual(test_query_set, test_search_1)
        self.assertQuerysetEqual(test_query_set, test_search_2)
        self.assertQuerysetEqual(test_query_set, test_search_3)
        self.assertQuerysetEqual(test_query_set, test_search_4)
        self.assertEqual(test_search_5.count(), 0)
        self.assertQuerysetEqual(test_query_set, test_search_6)
        self.assertQuerysetEqual(test_query_set, test_search_7)
        self.assertQuerysetEqual(test_query_set, test_search_8)

    def test_filter_search_listing(self):
        test_real_estate = RealEstate()
        test_real_estate.save()
        test_house = House(date_of_construction="1970-01-01",
            real_estate=test_real_estate)
        test_house.save()
        test_apartment = Apartment(
            is_primary=True,
            number_of_rooms=3,
            size_sq_m=50,
            has_internet=True,
            is_furnished=True,
            house=test_house
        )
        test_apartment.save()
        test_listing = Listing(
            listing_type="rental",
            rental_price=1000,
            security_deposit=3000,
            date_available="2022-06-04",
            minimum_months=6,
            maximum_months=24,
            number_of_people=3,
            pets_ok=True,
            apartment=test_apartment,
            pk=1
        )
        test_params = {
            "listing_type": "rental",
            "rental_price": 1200,
            "security_deposit": 3600,
            # "for_sale_price":
            # "minimum_down_payment":
            "earliest_date_available": "2022-06-01",
            "latest_date_available": "2022-07-01",
            "minimum_months": 3,
            "maximum_months": 36,
            "number_of_people": 4,
            "pets_ok": True,
            "is_primary": True,
            "number_of_rooms": 2,
            "size_sq_m": 30,
            "has_internet": True,
            "is_furnished": True,
            "date_of_construction": "1969-12-31"
        }

        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)

        self.assertQuerysetEqual(test_query_set, test_search)

        test_params['rental_price'] = 800
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('rental_price')
        test_params['security_deposit'] = 2000
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('security_deposit')
        test_params['listing_type'] = "for_sale"
        test_params['for_sale_price'] = 250000
        test_params['minimum_down_payment'] = 50000
        test_listing.listing_type = "for_sale"
        test_listing.for_sale_price = 200000
        test_listing.minimum_down_payment = 40000
        test_listing.save()
        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_query_set, test_search)

        test_params['for_sale_price'] = 150000
        test_params['minimum_down_payment'] = 30000
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('for_sale_price')
        test_params.pop('minimum_down_payment')

        test_params['earliest_date_available'] = "2022-06-05"
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('earliest_date_available')
        test_params['latest_date_available'] = "2022-06-03"
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('latest_date_available')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['minimum_months'] = 7
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('minimum_months')
        test_params['maximum_months'] = 12
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('maximum_months')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['number_of_people'] = 2
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('number_of_people')
        test_params['pets_ok'] = False
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('pets_ok')
        test_params['is_primary'] = False
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('is_primary')
        test_params['number_of_rooms'] = 4
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('number_of_rooms')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['size_sq_m'] = 60
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('size_sq_m')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_listing.apartment.has_internet = False
        test_listing.apartment.save()
        test_listing.save()
        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('has_internet')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_listing.apartment.is_furnished = False
        test_listing.apartment.save()
        test_listing.save()
        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('is_furnished')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['date_of_construction'] = "1970-01-02"
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('date_of_construction')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)
