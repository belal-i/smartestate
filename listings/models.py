from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator,
    validate_comma_separated_integer_list
)

from datetime import date

from broker.models import *

# Create your models here.




class Listing(models.Model):

    # TODO: See Feature #346
    #       Either deprecate this, or implement support for this relation
    #       in our views.
    house = models.ForeignKey('House', on_delete=models.CASCADE, 
        null=True, blank=True)

    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, 
        null=True, blank=True)

    # TODO: See Feature #343. Make this ManyToMany?
    contact = models.ForeignKey('broker.Contact', on_delete=models.CASCADE, 
        null=True, blank=True)
    # TODO: Figure out how to translate these choices.
    LISTING_TYPE_CHOICES = (
        ('rental','RENTAL'),
        ('for_sale','FOR_SALE'),
    )
    listing_type = models.CharField(max_length=8,
        choices=LISTING_TYPE_CHOICES, default='rental')
    currency = models.CharField(max_length=4, default='$')
    rental_price = models.DecimalField(max_digits=7, decimal_places=2,
        null=True, blank=True)
    security_deposit = models.DecimalField(max_digits=7, decimal_places=2,
        null=True, blank=True)
    info_about_rental_price = models.CharField(max_length=64,
         blank=True, null=True, default='Does not include utilities')
    for_sale_price = models.DecimalField(max_digits=10, decimal_places=2,
        null=True, blank=True)
    minimum_down_payment = models.DecimalField(max_digits=10, decimal_places=2,
        null=True, blank=True)
    short_description = models.CharField(max_length=128,
        default='A beautiful new vacancy',
        help_text='A short description of your listing')
    long_description = models.TextField(max_length=1024, default='',
        null=True, blank=True,
        help_text='A detailed description of your listing')
    date_available = models.DateField(default=date.today)
    minimum_months = models.PositiveIntegerField(default=3,
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(128)])
    maximum_months = models.PositiveIntegerField(default=60,
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(128)])

    # TODO: See Feature #383.
    number_of_people = models.PositiveIntegerField(default=1,
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(20)])

    limitations = models.CharField(max_length=256, null=True, blank=True,
        default='', help_text='Limiting factors to qualify for approval \
            (no smoking, must be full-time employee, etc.)')
    pets_ok = models.BooleanField(default=False)
    def __str__(self):
        return self.short_description

class RealEstate(models.Model):
    address = models.OneToOneField('broker.Address', on_delete=models.CASCADE,
        null=True)
    surroundings = models.TextField(max_length=1024, null=True, blank=True)
    def __str__(self):
        return self.address.__str__()

class House(models.Model):
    # Can we have several houses on one single property? I don't think so.
    # That's why this is one-to-one.
    real_estate = models.OneToOneField('RealEstate', on_delete=models.CASCADE,
        primary_key=True)
    number_of_stories = models.PositiveIntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    date_of_construction = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.real_estate.__str__()

class Apartment(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    number_of_rooms = models.PositiveIntegerField(default=3,
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    size_sq_m = models.PositiveIntegerField(default=30,
        validators=[MinValueValidator(1), MaxValueValidator(500)])
    story = models.CharField(default="0", max_length=7,
        validators=[validate_comma_separated_integer_list])
    room_details = models.TextField(max_length=1024,
        null=True, blank=True)
    is_furnished = models.BooleanField(default=False)

    # TODO: See Feature #369.
    #       Turn these into drop down fields with predefined choirces,
    #       then you can implement support for them in
    #       broker.utils.filter_search_listing.
    flooring = models.CharField(max_length=128, null=True, blank=True)
    furnishing = models.TextField(max_length=512,
        null=True, blank=True)

    kitchen_info = models.TextField(max_length=512,
        null=True, blank=True)
    technical_equipment = models.TextField(max_length=512,
        null=True, blank=True, help_text='Washing machine, dryer, TV, etc.')
    has_internet = models.BooleanField(default=True)
    internet_info = models.CharField(max_length=256, null=True, blank=True)
    specials = models.TextField(max_length=512, null=True, blank=True,
        help_text='Extra features that make this apartment attractive')
    def __str__(self):
        return self.house.__str__()

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/listings/', default='assets/house.jpg')
    image_name = models.CharField(max_length=32, default='untitled')
    real_estate = models.ForeignKey('RealEstate', on_delete=models.CASCADE,
        null=True, blank=True)
    house = models.ForeignKey('House', on_delete=models.CASCADE,
        null=True, blank=True)
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE,
        null=True, blank=True)
    listing = models.ManyToManyField('Listing')
    def __str__(self):
        return self.image_name

