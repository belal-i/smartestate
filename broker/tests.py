from django.test import TestCase

from .utils import *
from listings.models import *
from .models import *


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
        test_listing.save()
        test_params = {
            "listing_type": "rental",
            "max_rental_price": 1200,
            "max_security_deposit": 3600,
            "min_rental_price": 800,
            "min_security_deposit": 2400,
            # "for_sale_price":
            # "minimum_down_payment":
            "earliest_date_available": "2022-06-01",
            "latest_date_available": "2022-07-01",
            "minimum_months": 3,
            "maximum_months": 36,
            "max_number_of_people": 4,
            "min_number_of_people": 2,
            "pets_ok": True,
            "is_primary": True,
            "min_number_of_rooms": 2,
            "max_number_of_rooms": 4,
            "min_size_sq_m": 30,
            "max_size_sq_m": 60,
            "has_internet": True,
            "is_furnished": True,
            "min_date_of_construction": "1969-12-31",
            "max_date_of_construction": "1971-12-31",
        }

        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)

        self.assertQuerysetEqual(test_query_set, test_search)

        test_params['max_rental_price'] = 800
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_rental_price')
        test_params.pop('min_rental_price')
        test_params['max_security_deposit'] = 2000
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_security_deposit')
        test_params.pop('min_security_deposit')
        test_params['listing_type'] = "for_sale"
        test_params['max_for_sale_price'] = 250000
        test_params['max_minimum_down_payment'] = 50000
        test_listing.listing_type = "for_sale"
        test_listing.for_sale_price = 200000
        test_listing.minimum_down_payment = 40000
        test_listing.save()
        test_query_set = Listing.objects.filter(pk=1)
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_query_set, test_search)

        test_params['max_for_sale_price'] = 150000
        test_params['max_minimum_down_payment'] = 30000
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_for_sale_price')
        test_params.pop('max_minimum_down_payment')

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

        test_params['max_number_of_people'] = 2
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_number_of_people')
        test_params['pets_ok'] = False
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('pets_ok')
        test_params['is_primary'] = False
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('is_primary')
        test_params['min_number_of_rooms'] = 4
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('min_number_of_rooms')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_size_sq_m'] = 60
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('min_size_sq_m')
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

        test_params['min_date_of_construction'] = "1970-01-02"
        test_search = filter_search_listing(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('min_date_of_construction')
        test_search = filter_search_listing(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)


    def test_filter_search_seeking(self):
        # Make test Contact 30 years old.
        test_dob = datetime.datetime.now() - datetime.timedelta(days=30*365)
        #test_dob = test_dob.strftime("%Y-%M-%d") ???? ########
        year = str(test_dob.year)
        month = str(test_dob.month)
        day = str(test_dob.day)
        test_dob = year + "-" + month + "-" + day
        ##############
        test_contact = Contact(date_of_birth=test_dob)
        test_contact.save()
        test_seeking = Seeking(
            seeking_type="rental",
            max_rent=1000,
            max_purchase_price=250000,
            min_number_of_rooms=3,
            min_size_sq_m=50,
            number_of_persons=3,
            starting_date="2022-07-01",
            ending_date="2022-10-01",
            number_of_months=3,
            must_be_furnished=True,
            must_have_internet=True,
            is_smoker=True,
            has_pets=True,
            contact=test_contact,
            pk=1
        )
        test_seeking.save()

        test_params = {
            "seeking_type": "rental",
            "max_rent": 1200,
            "min_rent": 500,
            # "max_purchase_price":
            # "min_purchase_price":
            "min_number_of_rooms": 2,
            "max_number_of_rooms": 4,
            "min_size_sq_m": 40,
            "max_size_sq_m": 60,
            "min_number_of_persons": 2,
            "max_number_of_persons": 4,
            "min_starting_date": "2022-06-01",
            "max_starting_date": "2022-08-01",
            "min_ending_date": "2022-09-01",
            "max_ending_date": "2022-11-01",
            "min_number_of_months": 2,
            "max_number_of_months": 4,
            "must_be_furnished": True,
            "must_have_internet": True,
            "is_smoker": True,
            "has_pets": True,
            "min_age": 29,
            "max_age": 31,
        }

        test_query_set = Seeking.objects.filter(pk=1)

        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_query_set, test_search) 
        test_params['max_rent'] = 800
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_rent')
        test_params['min_rent'] = 1200
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('min_rent')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_query_set, test_search)

        test_params['seeking_type'] = "for_sale"
        test_params['max_purchase_price'] = 300000
        test_params['min_purchase_price'] = 200000
        test_seeking.seeking_type = "for_sale"
        test_seeking.save()
        test_query_set = Seeking.objects.filter(pk=1)
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_query_set, test_search) 

        test_params['max_purchase_price'] = 200000
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('max_purchase_price')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_purchase_price'] = 300000
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)

        test_params.pop('min_purchase_price')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_number_of_rooms'] = 4
        test_params['max_number_of_rooms'] = 2
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_number_of_rooms')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_number_of_rooms')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_size_sq_m'] = 60
        test_params['max_size_sq_m'] = 40
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_size_sq_m')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_size_sq_m')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_number_of_persons'] = 4
        test_params['max_number_of_persons'] = 2
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_number_of_persons')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_number_of_persons')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_starting_date'] = "2022-08-01"
        test_params['max_starting_date'] = "2022-06-01"
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_starting_date')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_starting_date')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_ending_date'] = "2022-11-01"
        test_params['max_ending_date'] = "2022-09-01"
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_ending_date')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_ending_date')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_number_of_months'] = 4
        test_params['max_number_of_months'] = 2
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_number_of_months')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_number_of_months')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['must_be_furnished'] = False
        test_params['must_have_internet'] = False
        test_params['is_smoker'] = False
        test_params['has_pets'] = False
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_seeking.must_be_furnished = False
        test_seeking.must_have_internet = False
        test_seeking.is_smoker = False
        test_seeking.has_pets = False
        test_seeking.save()
        test_query_set = Seeking.objects.filter(pk=1)
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)

        test_params['min_age'] = 31
        test_params['max_age'] = 29
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('min_age')
        test_search = filter_search_seeking(test_params)
        self.assertEqual(test_search.count(), 0)
        test_params.pop('max_age')
        test_search = filter_search_seeking(test_params)
        self.assertQuerysetEqual(test_search, test_query_set)


    def test_filter_search_matching(self):

        test_seeking = Seeking(
            seeking_type="rental",
            max_rent=1000,
            max_purchase_price=250000,
            min_number_of_rooms=3,
            min_size_sq_m=50,
            number_of_persons=3,
            starting_date="2022-07-01",
            ending_date="2022-10-01",
            number_of_months=3,
            must_be_furnished=True,
            must_have_internet=True,
            is_smoker=True,
            has_pets=True,
            # contact=test_contact,
            pk=2
        )
        test_seeking.save()

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
            pk=3
        )
        test_listing.save()

        test_matching = Matching(
            listing=test_listing,
            seeking=test_seeking,
            pk=1
        )
        test_matching.save()

        test_params = {
            "listing_id": 3,
            "seeking_id": 2,
        }
        test_query_set = Matching.objects.filter(pk=1)
        test_search_result = filter_search_matching(test_params)
        self.assertQuerysetEqual(test_query_set, test_search_result)

        test_params.pop("listing_id")
        test_search_result = filter_search_matching(test_params)
        self.assertQuerysetEqual(test_query_set, test_search_result)

        test_params = {
            "listing_id": 2,
            "seeking_id": 2,
        }

        test_search_result = filter_search_matching(test_params)
        self.assertEqual(test_search_result.count(), 0)
