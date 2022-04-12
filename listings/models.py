from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, \
    validate_comma_separated_integer_list

from config.models import Config

from datetime import date

# Create your models here.



################
# Real Estates #
################

class Listing(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE, 
        null=True, blank=True)
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, 
        null=True, blank=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, 
        null=True, blank=True)
    LISTING_TYPE_CHOICES = (
        ('rental','RENTAL'),
        ('for_sale','FOR_SALE'),
    )
    listing_type = models.CharField(max_length=8,
        choices=LISTING_TYPE_CHOICES, default='rental')
    currency = models.CharField(max_length=4,
        default=Config.objects.get_or_create(
            config_var='default_currency'
        )[0].config_val
    )
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
    address = models.OneToOneField('Address', on_delete=models.CASCADE,
        primary_key=True)
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


############
# Contacts #
############

class Contact(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=32)
    address = models.ManyToManyField('Address', blank=True)
    phone = models.ManyToManyField('Phone', blank=True)
    email = models.ManyToManyField('Email', blank=True)
    company = models.ManyToManyField('Company', blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    street = models.CharField(max_length=32)
    number = models.CharField(max_length=8, null=True, blank=True)
    zip_code = models.CharField(max_length=16, null=True, blank=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        # TODO: Quick fix...
        try:
            return self.street + ", " + self.zip_code + " " + self.city
        except TypeError:
            return "-"


class Phone(models.Model):
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.value

class Email(models.Model):
    # TODO: EmailField
    value = models.EmailField(max_length=40)
    def __str__(self):
        return self.value

class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.ManyToManyField('Address', blank=True)
    def __str__(self):
        return self.name
