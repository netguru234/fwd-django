from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact-us/', views.contact, name="contact"),
    path('truckloads/', views.truckloads, name="truckloads"),
    path('ltl/', views.ltl, name="ltl"),
    path('air/', views.air, name="air"),
    path('ocean/', views.ocean, name="ocean"),
    path('intermodal/', views.intermodal, name="intermodal"),
    path('track-consignment/', views.track, name="track"),
    # path('track-consignment/<str:tracking_number>/', views.track, name="track"),
    path('track-result/', views.result, name="result"),
    # path('', views.home, name="home"),
]
