from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.utils import translation

from smartestate.settings import *
from smartestate.functions import tuple_list_has_key
from listings.models import *
from .models import *
from .forms import ListingSearchForm, SeekingSearchForm


def start(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())


    if not request.user.is_authenticated:
                                       # Instead of /admin/, maybe do something like
                                       # settings.LOGIN_URL, but right now it does
                                       # not work. See: https://docs.djangoproject.com/en/4.0/topics/auth/default/
        return redirect('%s?next=%s' % ('/admin/', request.path))
    listings = Listing.objects.all()[:10]
    seekings = Seeking.objects.all()[:10]
    # TODO: See Feature #345. 
    #       For now, excluding closed matchings from this view, because
    #       sorting them would put closed matchings at the top.
    #       But in the future, we might figure out how to sort them in
    #       order of 'pending', 'possible', 'closed'.
    matchings = Matching.objects.filter(~Q(status='closed')).order_by(
        'status')[:10]
    context = {
        'listings': listings,
        'seekings': seekings,
        'matchings': matchings,
    }
    return render(request, 'broker/start.html', context)

def listings(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/admin/', request.path))
    listings = Listing.objects.all()
    listing_form = ListingSearchForm()
    return render(request, 'broker/listings.html',
        {'listings': listings, 'form': listing_form}
    )

def seekings(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/admin/', request.path))
    seekings = Seeking.objects.all()
    seekings_form = SeekingSearchForm()
    return render(request, 'broker/seekings.html',
        {'seekings': seekings, 'form': seekings_form}
    )

def matchings(request):
    # TODO: How to make it so that this does not need to be
    #       in every view?
    language = request.GET.get('language')
    if language is not None and tuple_list_has_key(LANGUAGES, language):
        translation.activate(language)
        request.session['language'] = language
    else:
        try:
            translation.activate(request.session['language'])
        except KeyError:
            translation.activate(translation.get_language())

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/admin/', request.path))
    matchings = Matching.objects.all()
    return render(request, 'broker/matchings.html', {'matchings': matchings})
