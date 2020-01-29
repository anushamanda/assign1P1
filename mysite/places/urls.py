from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='places'),
    path('place', views.place, name='place'),
    path('search', views.search, name='search'),
]