from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ConfigTranslationOptions(TranslationOptions):
    fields = (
        'cover_text',
    )

translator.register(Config, ConfigTranslationOptions)
