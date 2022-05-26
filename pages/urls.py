from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('<str:page_name>', views.single_page, name='single_page'),
]
