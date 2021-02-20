from django.urls import path
import json
from . import views

urlpatterns = [


    path('index', views.home),
    # this search is for returning the search results to the same search page
    path('search/search', views.search, name="search"),
    # this search is for going form the nav bar to the search page
    path('search/', views.searchlink),

    path('login/', views.login),
    #path('signup/', views.signup),
    path('', views.form),
]
