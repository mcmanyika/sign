from django.urls import path

from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('search-sign', showresults, name='search_sign'),
]