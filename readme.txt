Setting up:

You have to set up the cookie group in the Django admin, and make it optional, for the cookie banner to appear.

Requirements:

Django 4.0 (Note about Defect #452: We can't use 4.1 until django-cookie-consent 0.3.2 is released.
            To install Django 4.0 locally: python3 -m pip install Django==4.0, or to override
            an already installed newer version: python3 -m pip install -Iv Django==4.0)
datetime
Pillow
django-cookie-consent (See https://pypi.org/project/django-cookie-consent/, https://github.com/jazzband/django-cookie-consent)
djangorestframework
django-widget-tweaks
