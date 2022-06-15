from django import forms

class ListingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_listing

    listing_type = forms.ChoiceField(choices=[
        ('rental', 'Rental'),
        ('for_sale', 'For sale')
        ], label='Listing type',
        widget=forms.Select(attrs={'class': 'form-toggle-field'})
    )
    max_rental_price = forms.IntegerField(label='Maximum rental price')
    min_rental_price = forms.IntegerField(label='Minimum rental price')
    max_security_deposit = forms.IntegerField(label='Maximum security deposit')
    min_security_deposit = forms.IntegerField(label='Minimum security deposit')
    max_for_sale_price = forms.IntegerField(label='Maximum for sale price')
    min_for_sale_price = forms.IntegerField(label='Minimum for sale price')
    max_minimum_down_payment = forms.IntegerField(
        label='Highest acceptable minimum down payment'
    )
    min_minimum_down_payment = forms.IntegerField(
        label='Lowest acceptable minimum down payment'
    )
    earliest_date_available = forms.DateField(
        label='Earliest date available'
    )
    latest_date_available = forms.DateField(
        label='Latest date available'
    )
    minimum_months = forms.IntegerField(
        label='Minimum number of months available'
    )
    maximum_months = forms.IntegerField(
        label='Maximum number of months available'
    )
    min_number_of_people = forms.IntegerField(
        label='Minimum number of people'
    )
    max_number_of_people = forms.IntegerField(
        label='Maximum number of people'
    )
    pets_ok = forms.BooleanField(
        label='Pets OK',
        required=False,
    )
    is_primary = forms.BooleanField(
        label='Apartment is the only / primary one in the house',
        required=False,
    )
    min_number_of_rooms = forms.IntegerField(
        label='Minimum number of rooms'
    )
    max_number_of_rooms = forms.IntegerField(
        label='Maximum number of rooms'
    )
    min_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters'
    )
    max_size_sq_m = forms.IntegerField(
        label='Maximum size in square meters'
    )
    has_internet = forms.BooleanField(
        label='Internet is included',
        required=False,
    )
    is_furnished = forms.BooleanField(
        label='Apartment must be furnished',
        required=False,
    )
    min_date_of_construction = forms.DateField(
        label='Earliest acceptable date of construction'
    )
    max_date_of_construction = forms.DateField(
        label='Latest acceptable date of construction'
    )

class SeekingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_seeking

    seeking_type = forms.ChoiceField(choices=[
        ('rental', 'Rental'),
        ('for_sale', 'For sale')
        ], label='Seeking type',
        widget=forms.Select(attrs={'class': 'form-toggle-field'})
    )
    max_rent = forms.IntegerField(label='Maximum acceptable rent')
    min_rent = forms.IntegerField(label='Minimum acceptable rent')
    max_purchase_price = forms.IntegerField(
        label='Maximum acceptable purchase price'
    )
    min_purchase_price = forms.IntegerField(
        label='Minimum acceptable purchase price'
    )
    min_number_of_rooms = forms.IntegerField(
        label='Minimum number of rooms'
    )
    max_number_of_rooms = forms.IntegerField(
        label='Maximum number of rooms'
    )
    min_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters'
    )
    max_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters'
    )
    min_number_of_persons = forms.IntegerField(
        label='Minimum number of persons'
    )
    max_number_of_persons = forms.IntegerField(
        label='Maximum number of persons'
    )
    min_starting_date = forms.DateField(
        label='Earliest possible starting date'
    )
    max_starting_date = forms.DateField(
        label='Latest possible starting date'
    )
    min_ending_date = forms.DateField(
        label='Earliest possible ending date'
    )
    max_ending_date = forms.DateField(
        label='Latest possible ending date'
    )
    min_number_of_months = forms.IntegerField(
        label='Minimum number of months'
    )
    max_number_of_months = forms.IntegerField(
        label='Maximum number of months'
    )
    must_be_furnished = forms.BooleanField(
        label='Apartment must be furnished',
        required=False
    )
    must_have_internet = forms.BooleanField(
        label='Must have internet',
        required=False
    )
    is_smoker = forms.BooleanField(
        label='Tenant is smoker',
        required=False
    )
    has_pets = forms.BooleanField(
        label='Tenant has pets',
        required=False
    )
    min_age = forms.IntegerField(
        label='Minimum age of tenant'
    )
    max_age = forms.IntegerField(
        label='Maximum age of tenant'
    )
