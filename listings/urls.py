from django.urls import path

from . import views

urlpatterns = [
    # Ex: listings/
    path('', views.list_redirect, name='list_redirect'),
    # Ex: listings/5
    path('<int:listing_id>', views.detail, name='detail'),
]
