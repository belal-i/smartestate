from listings.models import *
from broker.models import *
from rest_framework import serializers

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'street',
            'number',
            'zip_code',
            'city',
            'state',
            'country',
        ]
class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = [
            'value',
        ]
class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = [
            'value',
        ]

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=True)
    class Meta:
        model = Company
        fields = [
            'name',
            'address',
        ]
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=True)
    company = CompanySerializer(many=True)
    phone = PhoneSerializer(many=True)
    email = EmailSerializer(many=True)
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'address',
            'company',
            'phone',
            'email',
        ]

class RealEstateSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = RealEstate
        fields = [
            'surroundings',
            'address',
        ]

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    real_estate = RealEstateSerializer()
    class Meta:
        model = House
        fields = [
            'number_of_stories',
            'date_of_construction',
            'real_estate',
        ]

class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    house = HouseSerializer()
    class Meta:
        model = Apartment
        fields = [
            'is_primary',
            'number_of_rooms',
            'size_sq_m',
            'story',
            'room_details',
            'flooring',
            'furnishing',
            'kitchen_info',
            'technical_equipment',
            'has_internet',
            'internet_info',
            'specials',
            'house',
        ]

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    apartment = ApartmentSerializer()
    contact = ContactSerializer()
    class Meta:
        model = Listing
        fields = [
            'id',
            'listing_type',
            'rental_price',
            'security_deposit',
            'info_about_rental_price',
            'for_sale_price',
            'minimum_down_payment',
            'short_description',
            'long_description',
            'date_available',
            'minimum_months',
            'maximum_months',
            'number_of_people',
            'limitations',
            'pets_ok',
            'apartment',
            'contact',
        ]


class SeekingSerializer(serializers.HyperlinkedModelSerializer):
    contact = ContactSerializer()
    class Meta:
        model = Seeking
        fields = [
            'id',
            'seeking_type',
            'max_rent',
            'max_purchase_price',
            'min_number_of_rooms',
            'min_size_sq_m',
            'number_of_persons',
            'starting_date',
            'ending_date',
            'number_of_months',
            'must_be_furnished',
            'occupation',
            'employer',
            'is_smoker',
            'has_pets',
            'notes',
            'contact_source',
            'contact',
        ]

class MatchingSerializer(serializers.HyperlinkedModelSerializer):
    listing = ListingSerializer()
    seeking = SeekingSerializer()
    class Meta:
        model = Matching
        fields = [
            'id',
            'status',
            'note',
            'listing',
            'seeking',
        ]
