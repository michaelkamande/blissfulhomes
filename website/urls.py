from django.urls import path

from . import views



urlpatterns = [
	path('', views.home, name = 'home'),
	path('contact/', views.contact, name = 'contact'),
	path('favorites/', views.favorites, name = 'favorites'),
	path('properties/', views.properties, name = 'properties'),
    path('property/<int:id>/', views.property, name = 'property'),
    path('rent/', views.rent, name = 'rent'),
    path('buy/', views.buy, name = 'buy'),
    path('appartments/', views.appartments, name = 'appartments'),
    path('houses/', views.houses, name = 'houses'),
    path('terrains/', views.terrains, name = 'terrains'),
    path('offices/', views.offices, name = 'offices'),
    path('property/publish/', views.publish, name = 'publish'),
]
