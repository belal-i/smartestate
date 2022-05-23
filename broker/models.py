from datetime import date

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Contact(models.Model):
    # TODO: Give an optional is_primary field, to help deal with models that
    #       have more than one contact?
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=32)
    address = models.ManyToManyField('Address', blank=True)
    phone = models.ManyToManyField('Phone', blank=True)
    email = models.ManyToManyField('Email', blank=True)
    company = models.ManyToManyField('Company', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
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
    value = models.EmailField(max_length=40)
    def __str__(self):
        return self.value

class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.ManyToManyField('Address', blank=True)
    def __str__(self):
        return self.name

class Seeking(models.Model):
    SEEKING_TYPE_CHOICES = (
        ('rental','RENTAL'),
        ('for_sale','FOR_SALE'),
    )
    seeking_type = models.CharField(max_length=8,
        choices=SEEKING_TYPE_CHOICES, default='rental')
    # TODO: Make this ManyToMany?
    # TODO: Perhaps implement a seeking_contact model, with some
    #       seeking-related info, and that has a relation to the 
    #       "plain" contact model.
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, 
        null=True, blank=True)
    max_rent = models.DecimalField(null=True, blank=True,
        max_digits=7, decimal_places=2)
    max_purchase_price = models.DecimalField(null=True, blank=True,
        max_digits=10, decimal_places=2)
    min_number_of_rooms = models.IntegerField(null=True, blank=True, default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    min_size_qm = models.IntegerField(null=True, blank=True, default=20,
        validators=[MinValueValidator(1), MaxValueValidator(500)])
    number_of_persons = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(12)])

    # TODO: Implement some automatic synchronization between these fields####
    starting_date = models.DateField(null=True, blank=True, default=date.today)
    ending_date = models.DateField(null=True, blank=True)
    number_of_months = models.IntegerField(null=True, blank=True)
    ####

    must_be_furnished = models.BooleanField(default=False)
    line_of_work = models.CharField(null=True, blank=True, max_length=64,
        help_text="Type of job that this tenant/buyer has")
    employer = models.ForeignKey(Company, on_delete=models.CASCADE,
        null=True, blank=True)
    is_smoker = models.BooleanField(default=False)
    has_pets = models.BooleanField(default=False)
    notes = models.TextField(max_length=2048, null=True, blank=True)
    contact_source = models.CharField(max_length=64, null=True, blank=True,
        help_text="How did this person find out about us?")

