from modeltranslation.translator import translator, TranslationOptions
from .models import *

class SeekingTranslationOptions(TranslationOptions):
    fields = (
        'occupation',
        'notes',
    )

class MatchingTranslationOptions(TranslationOptions):
    fields = (
        'status',
        'note',
    )

translator.register(Seeking,  SeekingTranslationOptions)
translator.register(Matching, MatchingTranslationOptions)
