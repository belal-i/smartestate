from rest_framework.views import exception_handler
from django.shortcuts import render

def se_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 403:
            response = render(None, 'rest/403.html', {})
            response.status_code = 403
        else:
            response.data['status_code'] = response.status_code
    return response
