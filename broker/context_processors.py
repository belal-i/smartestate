from .forms import ListingSearchForm

def listing_search_form(request):
    return {'listing_search_form': ListingSearchForm()}
