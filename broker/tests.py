from django.test import TestCase

from .utils import *
from listings.models import *
from .models import *

# Create your tests here.

class TestSearch(TestCase):
    def test_search_results(self):
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

        test_search_1 = keyword_search("Hello")
        test_search_2 = keyword_search("World")
        test_search_3 = keyword_search("Test")
        test_search_4 = keyword_search("Foo")
        test_search_5 = keyword_search("Bar")
        test_search_6 = keyword_search("Boo")

        self.assertQuerysetEqual(test_query_set, test_search_1)
        self.assertQuerysetEqual(test_query_set, test_search_2)
        self.assertQuerysetEqual(test_query_set, test_search_3)
        self.assertQuerysetEqual(test_query_set, test_search_4)
        self.assertQuerysetEqual(test_query_set, test_search_5)
        self.assertEqual(test_search_6.count(), 0)
