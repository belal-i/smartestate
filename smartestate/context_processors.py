from .settings import LANGUAGES

def languages(request):
    """
    languages = []
    for lang in LANGUAGES:
        languages.append(lang[0])
    return {'languages': languages}
    """
    return {'languages': LANGUAGES}
