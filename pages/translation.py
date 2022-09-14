from modeltranslation.translator import translator, TranslationOptions
from .models import *

class PageTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'nav_name',
        'content',
    )

translator.register(Page, PageTranslationOptions)
