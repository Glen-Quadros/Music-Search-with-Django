from django.urls import path
from .views import music_search, search_results

urlpatterns = [
    path('', music_search, name='music_search'),
    path('search/', search_results, name='search_results'),
]
