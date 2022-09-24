from django import forms
from django.utils.translation import gettext_lazy as _

class ListingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_listing

    listing_type = forms.ChoiceField(choices=[
        ('', '--'),
        ('rental', _('Rental')),
        ('for_sale', _('For sale')),
        ], label=_('Listing type'),
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rental_price = forms.IntegerField(label=_('Maximum rent'),
        required=False)
    min_rental_price = forms.IntegerField(label=_('Minimum rent'),
        required=False)
    max_security_deposit = forms.IntegerField(label=_('Maximum security deposit'),
        required=False)
    min_security_deposit = forms.IntegerField(label=_('Minimum security deposit'),
        required=False)
    max_for_sale_price = forms.IntegerField(label=_('Maximum for sale price'),
        required=False)
    min_for_sale_price = forms.IntegerField(label=_('Minimum for sale price'),
        required=False)
    max_minimum_down_payment = forms.IntegerField(
        label=_('Highest acceptable minimum down payment'),
        required=False
    )
    min_minimum_down_payment = forms.IntegerField(
        label=_('Lowest acceptable minimum down payment'),
        required=False
    )
    earliest_date_available = forms.DateField(
        label=_('Earliest date available'),
        required=False
    )
    latest_date_available = forms.DateField(
        label=_('Latest date available'),
        required=False
    )
    minimum_months = forms.IntegerField(
        label=_('Minimum number of months'),
        required=False
    )
    maximum_months = forms.IntegerField(
        label=_('Maximum number of months'),
        required=False
    )
    min_number_of_people = forms.IntegerField(
        label=_('Minimum number of people'),
        required=False
    )
    max_number_of_people = forms.IntegerField(
        label=_('Maximum number of people'),
        required=False
    )
    pets_ok = forms.BooleanField(
        label=_('Pets OK'),
        required=False,
    )
    is_primary = forms.BooleanField(
        label=_('Apartment is the only / primary one in the house'),
        required=False,
    )
    min_number_of_rooms = forms.IntegerField(
        label=_('Minimum number of rooms'),
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label=_('Maximum number of rooms'),
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label=_('Minimum size (sq. m)'),
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label=_('Maximum size (sq. m)'),
        required=False
    )
    has_internet = forms.BooleanField(
        label=_('Internet is included'),
        required=False,
    )
    is_furnished = forms.BooleanField(
        label=_('Apartment must be furnished'),
        required=False,
    )
    min_date_of_construction = forms.DateField(
        label=_('Earliest acceptable date of construction'),
        required=False
    )
    max_date_of_construction = forms.DateField(
        label=_('Latest acceptable date of construction'),
        required=False
    )

class SeekingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_seeking

    seeking_type = forms.ChoiceField(choices=[
        ('', '--'),
        ('rental', _('Rental')),
        ('for_sale', _('For sale')),
        ], label=_('Seeking type'),
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rent = forms.IntegerField(label=_('Maximum rent'),
        required=False)
    min_rent = forms.IntegerField(label=_('Minimum rent'),
        required=False)
    max_purchase_price = forms.IntegerField(
        label=_('Maximum purchase price'),
        required=False
    )
    min_purchase_price = forms.IntegerField(
        label=_('Minimum purchase price'),
        required=False
    )
    min_number_of_rooms = forms.IntegerField(
        label=_('Minimum number of rooms'),
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label=_('Maximum number of rooms'),
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label=_('Minimum size (sq. m)'),
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label=_('Maximum size (sq. m)'),
        required=False
    )
    min_number_of_persons = forms.IntegerField(
        label=_('Minimum number of persons'),
        required=False
    )
    max_number_of_persons = forms.IntegerField(
        label=_('Maximum number of persons'),
        required=False
    )
    min_starting_date = forms.DateField(
        label=_('Earliest starting date'),
        required=False
    )
    max_starting_date = forms.DateField(
        label=_('Latest starting date'),
        required=False
    )
    min_ending_date = forms.DateField(
        label=_('Earliest ending date'),
        required=False
    )
    max_ending_date = forms.DateField(
        label=_('Latest ending date'),
        required=False
    )
    min_number_of_months = forms.IntegerField(
        label=_('Minimum number of months'),
        required=False
    )
    max_number_of_months = forms.IntegerField(
        label=_('Maximum number of months'),
        required=False
    )
    must_be_furnished = forms.BooleanField(
        label=_('Apartment must be furnished'),
        required=False
    )
    must_have_internet = forms.BooleanField(
        label=_('Must have internet'),
        required=False
    )
    is_smoker = forms.BooleanField(
        label=_('Tenant is smoker'),
        required=False
    )
    has_pets = forms.BooleanField(
        label=_('Tenant has pets'),
        required=False
    )
    min_age = forms.IntegerField(
        label=_('Minimum age of tenant'),
        required=False
    )
    max_age = forms.IntegerField(
        label=_('Maximum age of tenant'),
        required=False
    )
