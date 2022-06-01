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
