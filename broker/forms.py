from django import forms

class ListingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_listing

    listing_type = forms.ChoiceField(choices=[
        ('', '--'),
        ('rental', 'Rental'),
        ('for_sale', 'For sale'),
        ], label='Listing type',
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rental_price = forms.IntegerField(label='Maximum rental price',
        required=False)
    min_rental_price = forms.IntegerField(label='Minimum rental price',
        required=False)
    max_security_deposit = forms.IntegerField(label='Maximum security deposit',
        required=False)
    min_security_deposit = forms.IntegerField(label='Minimum security deposit',
        required=False)
    max_for_sale_price = forms.IntegerField(label='Maximum for sale price',
        required=False)
    min_for_sale_price = forms.IntegerField(label='Minimum for sale price',
        required=False)
    max_minimum_down_payment = forms.IntegerField(
        label='Highest acceptable minimum down payment',
        required=False
    )
    min_minimum_down_payment = forms.IntegerField(
        label='Lowest acceptable minimum down payment',
        required=False
    )
    earliest_date_available = forms.DateField(
        label='Earliest date available',
        required=False
    )
    latest_date_available = forms.DateField(
        label='Latest date available',
        required=False
    )
    minimum_months = forms.IntegerField(
        label='Minimum number of months available',
        required=False
    )
    maximum_months = forms.IntegerField(
        label='Maximum number of months available',
        required=False
    )
    min_number_of_people = forms.IntegerField(
        label='Minimum number of people',
        required=False
    )
    max_number_of_people = forms.IntegerField(
        label='Maximum number of people',
        required=False
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
        label='Minimum number of rooms',
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label='Maximum number of rooms',
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters',
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label='Maximum size in square meters',
        required=False
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
        label='Earliest acceptable date of construction',
        required=False
    )
    max_date_of_construction = forms.DateField(
        label='Latest acceptable date of construction',
        required=False
    )

class SeekingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_seeking

    seeking_type = forms.ChoiceField(choices=[
        ('', '--'),
        ('rental', 'Rental'),
        ('for_sale', 'For sale'),
        ], label='Seeking type',
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rent = forms.IntegerField(label='Maximum acceptable rent',
        required=False)
    min_rent = forms.IntegerField(label='Minimum acceptable rent',
        required=False)
    max_purchase_price = forms.IntegerField(
        label='Maximum acceptable purchase price',
        required=False
    )
    min_purchase_price = forms.IntegerField(
        label='Minimum acceptable purchase price',
        required=False
    )
    min_number_of_rooms = forms.IntegerField(
        label='Minimum number of rooms',
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label='Maximum number of rooms',
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters',
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label='Minimum size in square meters',
        required=False
    )
    min_number_of_persons = forms.IntegerField(
        label='Minimum number of persons',
        required=False
    )
    max_number_of_persons = forms.IntegerField(
        label='Maximum number of persons',
        required=False
    )
    min_starting_date = forms.DateField(
        label='Earliest possible starting date',
        required=False
    )
    max_starting_date = forms.DateField(
        label='Latest possible starting date',
        required=False
    )
    min_ending_date = forms.DateField(
        label='Earliest possible ending date',
        required=False
    )
    max_ending_date = forms.DateField(
        label='Latest possible ending date',
        required=False
    )
    min_number_of_months = forms.IntegerField(
        label='Minimum number of months',
        required=False
    )
    max_number_of_months = forms.IntegerField(
        label='Maximum number of months',
        required=False
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
        label='Minimum age of tenant',
        required=False
    )
    max_age = forms.IntegerField(
        label='Maximum age of tenant',
        required=False
    )
