from django.urls import path

from . import views

urlpatterns = [
    # Ex: listings/
    path('', views.index, name='index'),
    # Ex: listings/5
    path('<int:listing_id>', views.detail, name='detail'),
]
