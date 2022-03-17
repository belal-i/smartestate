from django.urls import include, path
from . import views

app_name = "rest"
urlpatterns = [
    # path('', include(router.urls)),
    path('listings/', views.listings, name='listings'),
    path('seekings/', views.seekings, name='seekings'),
    path('matchings/', views.matchings, name='matchings'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
