import json
from pprint import pprint
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.request import Request
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)
from rest_framework.test import APIRequestFactory, APIClient

from listings.models import *
from broker.models import *


class RestSearch(TestCase):
    def test_post_matchings(self):
        listing = Listing(pk=2)
        seeking = Seeking(pk=3)
        listing.save()
        seeking.save()

        user = User.objects.create_user('testuser')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/rest/matchings/', {'listing_id': '2', 'seeking_id': '3'})
        content = json.loads(response.content.decode('utf8'))

        matching_id = content['id']
        matching = Matching.objects.get(pk=matching_id)

        self.assertEqual(matching.listing, listing)
        self.assertEqual(matching.seeking, seeking)

        response = client.post('/rest/matchings/', {'listing_id': '20', 'seeking_id': '30'})
        content = json.loads(response.content.decode('utf8'))

        self.assertEqual(response.status_code, 400)

        user.delete()
