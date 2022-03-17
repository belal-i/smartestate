from django.urls import path

from . import views

app_name = 'broker'

urlpatterns = [
    path('', views.start, name='start'),
    path('listings/', views.listings, name='listings'),
    path('seekings/', views.seekings, name='seekings'),
    path('matchings/', views.matchings, name='matchings'),
]
