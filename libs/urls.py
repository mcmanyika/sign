from django.urls import path

from .views import *

urlpatterns = [

    path('', showresults, name='search_sign'),
    path('index', index.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
]