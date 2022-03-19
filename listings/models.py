from django.db import models

# Create your models here.



################
# Real Estates #
################

class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    real_estate = models.ForeignKey('RealEstate', on_delete=models.CASCADE, 
        null=True, blank=True)
    house = models.ForeignKey('House', on_delete=models.CASCADE, 
        null=True, blank=True)
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, 
        null=True, blank=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, 
        null=True, blank=True)
    #rental_listing = models.OneToOneField('RentalListing',
    #    on_delete=models.CASCADE, null=True, blank=True)
    #for_sale_listing = models.OneToOneField('ForSaleListing',
    #    on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.real_estate.__str__()

class RentalListing(models.Model):
    rent = models.DecimalField(max_digits=7, decimal_places=2,
        null=True, blank=True)
    listing = models.OneToOneField('Listing', on_delete=models.CASCADE,
        null=True, blank=True)
    # TODO: This breaks the app
    def __str__(self):
        return self.listing.__str__()
    
class ForSaleListing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2,
        null=True, blank=True)
    listing = models.OneToOneField('Listing', on_delete=models.CASCADE,
        null=True, blank=True)
    # TODO: This breaks the app
    def __str__(self):
        return self.listing.__str__()

class RealEstate(models.Model):
    address = models.OneToOneField('Address', on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return self.address.__str__()

class House(models.Model):
    # Can we have several houses on one single property? I don't think so.
    # That's why this is one-to-one.
    real_estate = models.OneToOneField('RealEstate', on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return self.real_estate.__str__()

class Apartment(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE)
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
            return self.street + " " + self.number + ", " + self.city
        except TypeError:
            return "-"


class Phone(models.Model):
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.value

class Email(models.Model):
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.value

class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.ManyToManyField('Address', blank=True)
    def __str__(self):
        return self.name
