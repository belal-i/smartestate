from django.utils import translation
from .settings import LANGUAGES

def languages(request):
    return {'languages': LANGUAGES}

def current_language(request):
    try:
        current_language = request.session['language']
    except KeyError:
        current_language = translation.get_language()
    if current_language == "en-us":
        current_language = "en"
    return {'current_language': current_language}
