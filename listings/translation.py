from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ListingTranslationOptions(TranslationOptions):
    fields = (
        'listing_type',
        'info_about_rental_price',
        'short_description',
        'long_description',
        'limitations',
    )

class RealEstateTranslationOptions(TranslationOptions):
    fields = (
        'surroundings',
    )

class ApartmentTranslationOptions(TranslationOptions):
    fields = (
        'room_details',
        'flooring',
        'furnishing',
        'kitchen_info',
        'technical_equipment',
        'internet_info',
        'specials',
    )

class ImageTranslationOptions(TranslationOptions):
    fields = (
        'image_name',
    )

translator.register(Listing,    ListingTranslationOptions)
translator.register(RealEstate, RealEstateTranslationOptions)
translator.register(Apartment,  ApartmentTranslationOptions)
translator.register(Image,      ImageTranslationOptions)
